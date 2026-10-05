class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            my_list = [0] * 26
            for j in i:
                my_list[ord(j) - ord("a")] += 1 
            tuple_key = tuple(my_list)
            if tuple_key in dictionary:
                dictionary[tuple_key].append(i)
            else:
                dictionary[tuple_key] = [i]
        return list(dictionary.values())