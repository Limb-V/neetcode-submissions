# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:            # base case: already sorted
            return pairs
        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])    # sort the first half
        right = self.mergeSort(pairs[mid:])   # sort the second half
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        i = 0   # position of left's front
        j = 0   # position of right's front
        while i != len(left) and j != len(right):
            if left[i].key <= right[j].key:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged