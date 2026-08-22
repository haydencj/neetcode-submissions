class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern: (len of string)(delimiter)(string)
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        
        return s

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []

        i = 0
        while i < len(s):
            j = i
            # use j to find delimiter (start of string)
            while s[j] != "#":
                j += 1
            # get length, 'j' is exclusive
            size = int(s[i:j]) 
            start = j + 1
            end = start + size
            # capture string
            string = s[start:end]
            strs.append(string)
            # 'i' will be end of word
            i = end

        return strs