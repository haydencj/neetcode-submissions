class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            # if c is a close bracket, and stack has elements.
            if c in closeToOpen:
                # only pop if same type of bracket AND STACK EXISTS
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                # not same, we know false
                else: return False
            # if c is open bracket, add to stack
            else: 
                stack.append(c)
        
        print(stack)
        return False if stack else True 
