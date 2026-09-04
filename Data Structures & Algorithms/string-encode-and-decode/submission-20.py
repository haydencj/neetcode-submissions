class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern: (length)(delimiter)(string)
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string

        return s

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # i to j will be length (j exclusive)
            length = int(s[i:j])
            start = j + 1 # bc j will be at delimiter so add one
            end = start + length # will be 1 idx after end but ok bc exclusive
            string = s[start:end]
            strs.append(string)
            i = end

        return strs