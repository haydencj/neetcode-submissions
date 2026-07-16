class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern len(string) + delimiter + string
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        # two pointer ish approach to decode
        i = 0
        strs = []

        # 5#Hello5#World
        # len is 14, so we want to stop before we hit 13
        while i < len(s):
            j = i
            # find our delimiter
            while s[j] != "#":
                j += 1
            # we know size is the character before delimiter
            # we slice bc i should be at the end of our last word
            # if we didn't slice, we wouldn't catch a two digit number
            size = int(s[i:j]) + 1
            # last idx is exclusive in python slice so we add 1 to size
            string = s[j + 1 : j + size]
            strs.append(string)
            # set i to end of string
            i = j + size

        return strs