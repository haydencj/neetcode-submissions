class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use string manipulation to filter out non alphanumeric chars and convert to lowercase
        s = "".join(c.lower() for c in s if c.isalnum())
        #s = s.strip()
        print(s)

        i = 0
        j = len(s) - 1

        while i < j:
            print(i, j)
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True