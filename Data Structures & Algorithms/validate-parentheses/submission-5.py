class Solution:
    def isValid(self, s: str) -> bool:
        # push open brackets on stack, pop as we find their closing?
        closeToOpen = {")": "(", "}": "{", "]": "["}
        
        stack = [] * len(s)
        
        for c in s:
            if c in closeToOpen and len(stack):
                if closeToOpen[c] == stack[-1]:
                    stack.pop()
                else: return False
            else: stack.append(c)
        
        print(stack)
        return not bool(len(stack))
            
            

