from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_nums = 0
    for num in range(len(nums)):
        sum_nums += nums[num]
    return sum_nums
def get_min(nums: List[int]) -> int:
    min_nums = nums[0]
    for num in range(len(nums)):
        if min_nums < nums[num]:
            continue
        else:
            min_nums = nums[num]
    return min_nums
def get_max(nums: List[int]) -> int:
    max_nums = nums[0]
    for num in range(len(nums)):
        if max_nums > nums[num]:
            continue
        else:
            max_nums = nums[num]
    return max_nums

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
