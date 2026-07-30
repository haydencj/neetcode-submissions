class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            # if c is a closing bracket
            if c in closeToOpen and len(stack):
                if closeToOpen[c] == stack[-1]: # if the brackets pair, pop
                    stack.pop()
                else: # if they dont match, wrong order so false
                    return False
            # if c is open bracket
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False

