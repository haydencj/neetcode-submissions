class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern: (length of string)(delimiter)(string)...
        s = ""

        for string in strs:
            s += str(len(string)) + "#" + string
        
        print(s)
        return s

    # s = 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        # two pointer ish method
        i = 0
        res = []

        while i < len(s):
            j = i
            # find delimiter, start of a string
            while s[j] != "#":
                j += 1
            # found it. get size from i to j, since j will be exclusive
            # we dont worry about getting the delimiter, and it ensure's
            # we get double digit lengths
            # i should be at the end of last word
            size = int(s[i:j])
            start = j + 1
            end = start + size
            string = s[start:end]
            res.append(string)
            # set i to end of string position
            i = end

        return res