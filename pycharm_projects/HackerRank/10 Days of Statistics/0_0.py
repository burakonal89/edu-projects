# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_integers = int(raw_input())
number_string = str(raw_input())
number_list = [int(i) for i in number_string.split(" ")]
number_list.sort()
print number_list

mean = sum(number_list)/float(len(number_list))

if len(number_list)%2 == 0:
    median = (number_list[len(number_list)/2]+number_list[len(number_list)/2-1])/2.0
else:
    median = number_list[len(number_list)+1/2]

mode_dict = dict()
for i in number_list:
    if i not in mode_dict:
        mode_dict[i] = 0
    mode_dict[i] += 1

max_value = max(mode_dict.values())
max_keys = list()
for key in mode_dict:
    if mode_dict[key] == max_value:
        max_keys.append(key)
mode = min(max_keys)
print mean, median, mode