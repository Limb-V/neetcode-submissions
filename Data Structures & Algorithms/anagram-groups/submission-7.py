class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            string = "".join(sorted(i))
            if string in dictionary:
                dictionary[string].append(i)
            else:
                dictionary[string] = [i]
        return list(dictionary.values())