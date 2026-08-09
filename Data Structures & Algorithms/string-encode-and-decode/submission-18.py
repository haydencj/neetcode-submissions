class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern: (length of string)(delimiter)(string)
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        
        print(s)
        return s

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        strings = []
        # i will track end of string
        i = 0

        while i < len(s):
            j = i
            # j will find delimiter
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            string = s[start:end]
            strings.append(string)
            # set i to end of string
            i = end
            

        return strings