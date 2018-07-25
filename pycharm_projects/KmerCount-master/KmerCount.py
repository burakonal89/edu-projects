try:
    import mmh3
except ImportError:
    raise ImportError("requires mmh3 module, consider running 'sudo pip install mmh3'")
try:
    from pybloomfilter import BloomFilter as BF
except ImportError:
    raise ImportError("requires pybloomfilter module, consider running 'sudo pip install pybloomfiltermmap'")

import time
import argparse
import math
import sys
import heapq
import os

"""
KmerCount takes filename, kmersize and topcount from the user via terminal. Verbose is an optional command to see
elapsed time and memory usage for debugging purpose.
"""


class Heap(object):
    """
    A min heap implementation. A min heap is a tree structure that has the minimum value as the root. Min heap is used
    to find most frequent kmers in the data without explicitly sorting the whole hash table.
    """

    def __init__(self):
        self.heap = []

    def populate(self, n):
        for i in range(n):
            self.push((0, ""))

    def push(self, item):
        heapq.heappush(self.heap, item)

    def min(self):
        return self.heap[0][0]

    def pop(self):
        heapq.heappop(self.heap)

    def push_pop(self, item):
        heapq.heappushpop(self.heap, item)

    def nlargest(self, n):
        return heapq.nlargest(n, self.heap)


def calculate_parameters(total_kmer, disk_space, memory_space, kmer_size):
    """
    :param      kmer_total: The length of the input file
    :param      disk_space: Maximum allowed disk space usage.
    :param      memory_space: Maximum allowed memory usage.
    :param      kmer_size: The length of a kmer.
    :return:    unique_kmer: Maximum total number of unique kmers in the data.
                n_iter: Number of iterations necessary to write the data in allowed disk space.
                n_partition: Number of iterations necessary to read written data into memory in allowed memory space.
                bf_capacity: Number of items to be passed through the bloom filter.
                total_kmer_space: Total memory space necessary to keep all the unique kmers in the memory.
    """

    kmer_memory = kmer_size + sys.getsizeof("")  # size of each kmer (in bytes).
    kmer_disk = kmer_size + 1  # size of each kmer (in bytes) -including "\n" character at the end-.
    unique_kmer = total_kmer
    # number of unique kmer is decided based on total kmer number and kmer length.
    if math.log(4 ** kmer_size) < math.log(total_kmer):
        unique_kmer = 4 ** kmer_size
    n_iter = int(math.ceil(total_kmer * kmer_disk / disk_space))
    # memory load is bounded with 0.7 as suggested in the paper: http://minia.genouest.org/dsk/
    n_partition = int(math.ceil(unique_kmer * kmer_memory / (0.7 * memory_space * n_iter)))
    bf_capacity = int(math.ceil(total_kmer / (n_iter * n_partition)))
    total_kmer_memory = kmer_memory * unique_kmer
    return unique_kmer, n_iter, n_partition, bf_capacity, total_kmer_memory


def calculate_total_kmer(filename, kmer_size, verbose):
    """

    :param filename: File name to be processed.
    :param verbose: Option to print elapsed time.
    :return: Total kmer number in the file.
    """
    start = time.time()
    total_kmer = 0
    count = 0
    with open(filename) as f:
        for line in f:
            if count % 4 == 1:
                total_kmer += len(line) - kmer_size + 1
            count += 1
    end = time.time()
    if verbose:
        print ("Total kmer number in the file calculate in {0} seconds".format(end - start))
    return total_kmer


def dsk_with_bf(file_name, n_iter, n_partition, kmer_size, bf_capacity, bf_error, top_count, verbose):
    """
    Disk streaming of kmers with bloom filter.
    :param file_name: File to be processed.
    :param n_iter: Number of iterations to write kmers into disk.
    :param n_partition: Number of iterations to read files into memory.
    :param kmer_size: Length of the kmer.
    :param bf_capacity: Capacity of the bloom filter.
    :param bf_error: Probability of false positive in bloom filter.
    :param top_count: Number of kmers to be printed.
    :param verbose: Option to print elapsed time and memory usage.
    :return:
    """
    start_operation = time.time()
    # initialise a min heap
    h = Heap()
    h.populate(top_count)
    for iter_ in range(n_iter):
        start_iter = time.time()
        # initialise files where partitioned data is written.
        files = [open("{}".format(j), "w") for j in range(n_partition)]
        with open(file_name, "r") as file_from_read:
            count = 0
            for line in file_from_read:
                # take the second line to parse kmers.
                if count % 4 == 1:
                    line_length = len(line) - 1
                    for i in range(line_length - kmer_size + 1):
                        kmer = line[i:kmer_size + i]
                        # assign kmers to partitions.
                        hash_result = mmh3.hash(kmer)
                        if hash_result % n_iter == iter_:
                            # assign kmers to files
                            j = int((hash_result / n_iter) % n_partition)
                            files[j].write(kmer + "\n")
                count += 1
        for f in files:
            f.close()
        end = time.time()
        if verbose:
            print ("Disk write for iteration {0} done in {1} seconds".format(str(iter_), str(end - start_iter)))
        for j in range(n_partition):
            # initialise bloom filter
            bf = BF(bf_capacity, bf_error, "bf_dsk")
            start_partition = time.time()
            kmer_freq = dict()
            with open(str(j), "r") as f:
                for kmer in f:
                    if kmer in bf:
                        if kmer not in kmer_freq:
                            kmer_freq[kmer] = 1
                        kmer_freq[kmer] += 1
                    else:
                        bf.add(kmer)
            end = time.time()
            if verbose:
                print ("Hash table for iteration {0}, partition {1} done in {2} seconds.".format(str(iter_), str(j), str(
                    end - start_partition)))
                print ("Has table size for iteration {0} partition {1} is {2} Mb".format(str(iter_), str(j), str(
                    int(sys.getsizeof(kmer_freq)) / 10 ** 6)))

            start_heap = time.time()
            for kmer, freq in kmer_freq.items():
                if freq > h.min():
                    # h.pop()
                    # h.push((freq, kmer))
                    h.push_pop((freq, kmer))
            end = time.time()
            if verbose:
                print ("Heap done in {0} seconds".format(end - start_heap))
            # clean file and bf
            os.remove(str(j))
            os.remove("bf_dsk")
        end_iter = time.time()
        if verbose:
            print ("Iteration {0} done in {1} seconds.".format(str(iter_), str(end_iter - start_iter)))

    for item in h.nlargest(top_count):
        freq, kmer = item
        print (kmer[:-1], freq)
    end = time.time()
    if verbose:
        print ("Process done in {0} seconds.".format(str(end - start_operation)))


def hashtable_with_bf(file_name, kmer_size, bf_capacity, bf_error, top_count, verbose):
    """
     Hash table with bloom filter.
    :param file_name: File to be processed.
    :param kmer_size: Length of the kmer.
    :param bf_capacity: Capacity of the bloom filter.
    :param bf_error: Probability of false positive in bloom filter.
    :param top_count: Number of kmers to be printed
    :param verbose: Option to print elapsed time and memory usage.
    :return:
    """

    start = time.time()
    # initialise a min heap
    h = Heap()
    h.populate(top_count)
    # initialise bloom filter
    bf = BF(bf_capacity, bf_error, "hashtable_with_bf")
    kmer_freq = dict()
    with open(file_name, "r") as file_from_read:
        count = 0
        for line in file_from_read:
            # take the second line to parse kmers.
            if count % 4 == 1:
                line_length = len(line)
                for i in range(line_length - kmer_size + 1):
                    kmer = line[i:kmer_size + i]
                    if kmer in bf:
                        if kmer not in kmer_freq:
                            kmer_freq[kmer] = 1
                        kmer_freq[kmer] += 1
                    else:
                        bf.add(kmer)
            count += 1
    end = time.time()
    if verbose:
        print ("Hash table done in {0} seconds".format(end - start))
    start_heap = time.time()
    for kmer, freq in kmer_freq.iteritems():
        if freq > h.min():
            # h.pop()
            # h.push((freq, kmer))
            h.push_pop((freq, kmer))
    for item in h.nlargest(top_count):
        freq, kmer = item
        print (kmer, freq)
    end = time.time()
    # clean bf
    os.remove("hashtable_with_bf")
    if verbose:
        print ("Heap done in {0} seconds".format(end - start_heap))
        print ("Process done in {0} seconds".format(end - start))
        print ("Hash table size: {0} MB".format(int(sys.getsizeof(kmer_freq) / 10 ** 6)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", help="Specify the file name to be processed", type=str)
    parser.add_argument("--kmersize", help="Specify the kmer size", type=int)
    parser.add_argument("--topcount", help="Specify the number of top kmers to be displayed", type=int)
    parser.add_argument("--verbose", help="Printing elapsed time and memory usage for debugging purpose",
                        action="store_true")
    args = parser.parse_args()

    # Parameters
    disk_space = 5e10
    memory_space = 4e9
    # line_length = 90
    bf_error = 1e-2
    file_name = args.filename
    kmer_size = args.kmersize
    top_count = args.topcount
    verbose = args.verbose
    total_kmer = calculate_total_kmer(file_name, kmer_size, verbose=verbose)
    unique_kmer, n_iter, n_partition, bf_capacity, total_kmer_memory = calculate_parameters(total_kmer=total_kmer,
                                                                                            disk_space=disk_space,
                                                                                            memory_space=memory_space,
                                                                                            kmer_size=kmer_size)
    if verbose:
        print ("Total number of kmer: {0}".format(total_kmer))
        print ("Worst case unique number of kmer: {0}".format(unique_kmer))
        print ("Iteration number: {0}".format(str(n_iter)))
        print ("Partition number: {0}".format(str(n_partition)))
        print ("Bloom Filter capacity: {0}".format(str(bf_capacity)))

    if total_kmer_memory < 0.7 * memory_space:
        if verbose:
            print ("Hash table with Bloom Filter is running...")
        hashtable_with_bf(file_name=file_name,
                          kmer_size=kmer_size,
                          bf_capacity=bf_capacity,
                          bf_error=bf_error,
                          top_count=top_count,
                          verbose=verbose)

    else:
        if verbose:
            print ("DSK with Bloom Filter is running...")
        dsk_with_bf(file_name=file_name,
                    n_iter=n_iter,
                    n_partition=n_partition,
                    kmer_size=kmer_size,
                    bf_capacity=bf_capacity,
                    bf_error=bf_error,
                    top_count=top_count,
                    verbose=verbose)


if __name__ == '__main__':
    main()
