"""
Given a non-empty list of integers, every element appears twice except for one. Find that single one.

~ Solved by Eddy Ruhana
"""

intlist = [1, 1, 0, 2, 2, 3, 3, 5, 5, 4, 4]

enum_list = enumerate(intlist, 0)
duplicate_list = []

the_index = 0
index_limit = len(intlist)


for a, b in enum_list:
    the_index = a + 1

    while the_index < index_limit:
        if b == intlist[the_index]:
            duplicate_list.append(b)

        the_index += 1

for x in intlist:
    if x not in duplicate_list:
        print('The single element is: ', x)
