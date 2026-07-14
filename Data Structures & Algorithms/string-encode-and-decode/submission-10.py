class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
           s += str(len(string)) + '#' + string

        return s

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        print(s)

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            size = int(s[i:j]) + 1
            word = s[j+1:j+size]
            res.append(word)
            i=j+size

        return res