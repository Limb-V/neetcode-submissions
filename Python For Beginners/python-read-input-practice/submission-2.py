def add_two_numbers() -> int:
    line = input().split(",")
    num_sum = 0
    for i in line:
        num_sum += int(i)
    return num_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
