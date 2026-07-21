class Solution:

    def encode(self, strs: List[str]) -> str:
        # length + delimiter + string
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string

        print(s)
        return s 

    def decode(self, s: str) -> List[str]:
        res = []

        # i will give us start of length
        i = 0

        # 5#Hello5#World
        while i < len(s):
            j = i
            while s[j] != "#":
                # use j to find delimiter
                j += 1
                
            size = int(s[i:j]) + 1 # + 1 gets us last char from slice
            start = j + 1
            end = j + size

            string = s[start:end]
            res.append(string)

            # set i to end of word
            i = end


        return res