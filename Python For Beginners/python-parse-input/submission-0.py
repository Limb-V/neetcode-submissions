from typing import List

def read_integers() -> List[int]:
    line = input()
    line_list = line.split(",")
    num_list = []

    for i in line_list:
        num_list.append(int(i))
    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
