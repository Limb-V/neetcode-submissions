# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        my_list = []
        if pairs == []:
            return pairs
        my_list.append(pairs.copy())
        for i in range(1, len(pairs)):
            j = i 
            while j > 0 and pairs[j-1].key > pairs[j].key:
                tmp = pairs[j]
                pairs[j] = pairs[j-1]
                pairs[j-1] = tmp
                j -= 1
            my_list.append(pairs.copy())
        return my_list