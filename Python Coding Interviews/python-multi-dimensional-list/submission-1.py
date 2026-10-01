from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_num = 0
    my_list = []
    for i in nested_arr:
        for j in i:
            if max_num < j:
                max_num = j
        my_list.append(max_num)
    return my_list     
        


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
