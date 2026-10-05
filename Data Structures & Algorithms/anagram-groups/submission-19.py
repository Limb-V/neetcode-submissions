class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_dict = defaultdict(list)

        

        for st in strs:
            char_hash = [0]*26
            for char in st:
                char_hash[ord(char)-ord('a')] += 1
            
            str_dict[tuple(char_hash)].append(st)

            # if tuple(char_hash) in str_dict:
            #     str_dict[tuple(char_hash)].append(st)
            # else:
            #     str_dict[tuple(char_hash)] = [st]
            
        res = []

        for v in str_dict.values():
            res.append(v)

        return res
