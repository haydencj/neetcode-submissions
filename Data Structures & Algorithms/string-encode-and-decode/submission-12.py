class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern (len(string)) + (delimiter) + (string)
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string

        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # start of s

        while i < len(s): # ensures we dont go out of bounds
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j]) + 1
            string = s[j+1:j+size] 
            res.append(string)
            i = j + size
        
        return res