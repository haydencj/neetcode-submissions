class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use string manipulation to filter out non alphanumeric chars and convert to lowercase
        # s = "".join(c.lower() for c in s if c.isalnum())

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True

