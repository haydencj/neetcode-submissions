class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for c in s:
            # is it a close bracket?
            if c in closeToOpen:
                # if stack exists, and close matches top of stack, pop.
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                # either stack doesn't exist and we've seen a close (meaning false) 
                # or they don't match, so invalid and false
                else: return False
            # if its an open bracket add to stack
            else:
                stack.append(c)
        
        return False if stack else True
