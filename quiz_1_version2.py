# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

one_to_one_part_of_mapping = {}
mapping_as_a_list = []
nonkeys = []

for i in range(0, upper_bound):
    if i not in mapping:
        # 知识点：list.append()方法
        mapping_as_a_list.append(None)
        if i != 0:
            nonkeys.append(i)
    else:
        mapping_as_a_list.append(mapping[i])

# 计数器，记录每个value出现几次
counter_dict = {}
for item in mapping.items():
    counter_dict[item[1]] = counter_dict.get(item[1], 0) + 1

# 遍历mapping，选出value出现一次的key
# 知识点：dict.items()方法
for item in mapping.items():
    if counter_dict[item[1]] == 1:
        one_to_one_part_of_mapping[item[0]] = item[1]
print()
# google搜索"f-string"
# 知识点：内建len()函数
print(f'The mappings\'s so-called "keys" make up a set whose number of elements is {len(mapping)}.')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


