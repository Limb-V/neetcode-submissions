class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for st in strs:
            string += str(len(st))
            string += "#"
            string += st
        return string
           
    def decode(self, s: str) -> List[str]:
        string_list = []
        i = 0 
        j = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:length+j+1]
            string_list.append(word)
            i = length+j+1
        return string_list