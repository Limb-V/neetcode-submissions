def add_two_numbers() -> int:
    line = input().split(",")
    nums = []
    num_sum = 0
    for i in line:
        nums.append(int(i))
    for i in range(len(nums)):
        num_sum += nums[i]
    return num_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
