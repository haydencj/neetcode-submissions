class Solution:
    def isValid(self, s: str) -> bool:
        # basic idea: push open brackets onto stack, pop when see same close bracket
        # if stack is empty at the end? return true.

        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            # if close bracket
            if c in closeToOpen:
                # if stack is not empty (meaning theres an open bracket on stack)
                # and the top of stack matches close, then pop
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # else? invalid 
                else: 
                    return False
            # if open bracket
            else: 
                stack.append(c)
        
        return False if stack else True