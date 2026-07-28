class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern: (length)(delimiter)(string)
        s = ""

        for string in strs:
            s += str(len(string)) + "#" + string
        
        print(s)
        return s

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0

        # loop until i is at end of s
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            # from i:j we get size (j is exclusive)
            size = int(s[i:j])
            # start of word (1 idx after delimiter)
            start = j + 1
            # end of word (start + size)
            end = start + size
            # word is from start:end
            string = s[start:end]
            strings.append(string)
            # update i
            # var i should be 1 idx after end of word (which is end)
            i = end

        return strings