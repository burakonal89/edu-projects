KmerCount takes a FASTQ file as input along with k-mer length and number of top k-mers to be displayed and returns
most frequent k-mers in a genetic sequence. The script is written and tested on macOS Sierra version 10.12.3

--------------------------------
Python Distribution and Packages
--------------------------------
KmerCount is written under Python 2.7.12 |Anaconda 4.2.0 distribution. The script imports "mmh3" (MurmurHash3 implementation
on in Python, see: https://pypi.python.org/pypi/mmh3/2.0) and "pybloomfilter" (A bloom filter implementation in Python, 
see: http://axiak.github.io/pybloomfiltermmap/) modules. To install these modules:

    sudo pip install mmh3
    sudo pip install pybloomfiltermmap

---------------------------------------
Command Line Arguments and Input Format
---------------------------------------
The script can be run from the command line with file name, k-mer size and top k-mer number parameters. There is also an
optional argument "verbose" for debugging purpose to print elapsed time and memory usage of several stages at the code.

Example run:

    python KmerCount.py --filename "FileName" --kmersize 30 --topcount 25
    python KmerCount.py --filename "FileName" --kmersize 30 --topcount 25 --verbose

The input file format, FASTQ, is a text file format for storing biological sequences as a string of nucleotide codes
(e.g., A C T G) along with quality information for each code, and is a common output of DNA sequencing machines. The
file consists of sets of 4 lines, with the first being a sequence “ID”, the second being the sequence itself, the third
containing just a ‘+’ character, and the fourth containing quality information. More information and examples can be found:
https://en.wikipedia.org/wiki/FASTQ_format
An example of a 4 line format:

    @ERR047698.1 FCD0E65ABXX:2:1101:1214:2053/2
    AGGTAATTCTATTAGAAAAATGGTGTATGTATTTTTACTTACTAATGCAAAGTTTAACAATTACCACTTCATGTATTAAAAGATACTAAC
    +
    CCCDDFFFHHHHHJJIJJJJJIIFHHIJJIJJJJJJJJIIJJJIJJIJJIIHFHIIJJIJJJJJIJJJJJJJJHIJJJJJJJIIJJHHGH

A k-mer is a substring of length k. For example, in the DNA sequence string “CCCDDF", set of k-mers of length 3: 
[“CCC”, “CCD”, “CDD”, “DDF”]

----------------
Design Decisions
----------------

Below are the pre-defined parameters:

disk_space = 5e10
memory_space = 4e9
bf_error = 1e-2

For a given file and k-mer size, KmerCount calculates worst case number of unique k-mers in order to assess memory
consumption of the operation. If the memory consumption will be lower than the threshold, a hash table with bloom filter approach
is chosen. If the memory consumption will be higher than the threshold, disk streaming of k-mers with bloom filter approach
is chosen.

A reference paper about the implementation of bloom filter for k-mer counting can be seen here:
http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-12-333

------------
Bloom Filter
------------
A bloom filter (BF) is space efficient binary data structure, which is used to test whether an element is a member of a set.
An initial BF with length m is created consists of 0's only. Member to be added to the bloom filter is hashed k-times
and each hash result's modulo with respect to m is taken. The result is the index of the bit to be flipped to 1 in the BF.
Once all the members are added to the BF, a candidate is hashed k times, each hash result's modulo with respect to m is
taken and resulting index is checked whether it matches a 0 bit. If any of the hashed result matches with 0 bit,
the candidate cannot be in the set. If all of the hashed result matches with 1 bit, the candidate is probably in the set
as there can be collisions of the hashed results. The length of the BF is determined with respect to desired
error probability and the number of members of the set. For more information: https://en.wikipedia.org/wiki/Bloom_filter

KmerCount also uses "Disk Streaming of k-mers" method to process large files with specified memory and disk requirements.
The details of this method can ben seen here:
http://minia.genouest.org/dsk/

------------------------
Disk Streaming of k-mers
------------------------
The file is split into chunks whose total size is bounded by disk_space parameter. Each chunk is then written into files
on the disk, whose size is bounded by memory_space parameter. The distribution of k-mers to files is done via a hash function,
such that a specific k-mer can only be written into a specific file. This fact files to be separately counted to find
global list of k-mers. k-mers in each file is passed through a BF and put into a hash table only if they are seen in BF.
This avoids k-mers seen only once in the file to be added to hash table.

--------------------
Algorithmic Analysis
--------------------
With k-mer size 30 and top count 25, KmerCount is tested against "ERR047698.filt.fastq", "ERR055763_1.filt.fastq" and
"ERR047698_2.filt.fastq".

    file                        |  total k-mers |  iteration  | partition   | run time   |   hash table memory   |
    "ERR047698.filt.fastq"      |   ~12.2M      |       1     |     1       | 17.7 sec   |       25Mb            |
    "ERR055763_1.filt.fastq"    |   ~1.06B      |       1     |     26      | 2711.3 sec |       100Mb           |
    "ERR047698_2.filt.fastq"    |   ~4.3B       |       3     |     35      | 18244.5 sec|       100Mb           |

Note: Kamer Kaya has a very nice talk about Data Structures and Algorithms for Big Data. Video is available here:
https://www.youtube.com/watch?v=s8wDmKW19a4


