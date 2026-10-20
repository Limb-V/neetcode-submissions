# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        result = []
        for i in range(len(pairs)):
            reconstruction = self.calcgoon(i, pairs)
            result.append(reconstruction)
        return result

    def calcgoon(self, sortIndex, pairs):
        # important part
        goon = pairs[sortIndex]
        i = sortIndex - 1
        while i >= 0 and goon.key < pairs[i].key:
            pairs[i + 1] = pairs[i]
            i -= 1
        pairs[i + 1] = goon
        return pairs[:]

