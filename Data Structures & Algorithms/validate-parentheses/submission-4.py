class Solution:
    def isValid(self, s: str) -> bool:
        # edge case: length is odd
        if len(s) % 2 == 1: return False
        # push open brackets on stack, pop as we find their closing?
        close = {")": "(", "}": "{", "]": "["}
        
        stack = [] * len(s)
        
        for c in s:
            if c in close and len(stack):
                if close[c] == stack[-1]:
                    stack.pop()
                else: return False
            else: stack.append(c)
        
        print(stack)
        return not bool(len(stack))
            
            

