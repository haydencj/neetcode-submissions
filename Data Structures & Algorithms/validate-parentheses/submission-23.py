class Solution:
    def isValid(self, s: str) -> bool:
        # used to compare brackets
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            # if closing bracket
            if c in closeToOpen:
                # if stack exists, and have valid pair of brackets, pop
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                # stack is empty and we've already seen a closing (invalid order), false
                # or not valid pair of brackets, false
                else: return False
            # else it must be opening bracket
            else: stack.append(c)
        
        # for edge cases we must make sure stack is empty when returning true
        return True if not stack else False
