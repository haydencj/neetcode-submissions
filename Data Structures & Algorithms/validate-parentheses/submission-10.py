class Solution:
    def isValid(self, s: str) -> bool:
        # idea: as we see opening brackets, push on stack
        # as we see their corresponding closing, pop off stack
        # if stack is empty at the end, return true
        # if we see a closing bracket that DOES NOT equal an opening bracket, return false

        close = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in close:
                stack.append(c)
            elif stack and close[c] == stack[-1]:
                stack.pop()
            else: return False
            print(stack)

        print(stack)
        return True if not stack else False