class Solution:

    def encode(self, strs: List[str]) -> str:
        # pattern: (length)(delimiter)(string)...
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        
        print(s)
        return s
    
    # 5#Hell5o#World
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        # ensures we break before len(s) + 1, which would be out of bounds
        while i < len(s):
            j = i
            # use j to find delimiter
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            start = j + 1
            end = size + start # end is one idx after last char in string
            string = s[start:end] # ^^ is okay bc slice second idx is exclusive
            strs.append(string) 
            # var i should be 1 idx after end of string
            i = end
            
        return strs