class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            longest = 0
        else:
            num_set = set(nums)
            current = 1
            longest = 1
            for n in num_set:
                count = 1
                if (n-1) not in num_set:    
                    current = n
                    while (current + 1) in num_set:
                        current += 1
                        count += 1
                if count > longest:
                    longest = count
        return longest