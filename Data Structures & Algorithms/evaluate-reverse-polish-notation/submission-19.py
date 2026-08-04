class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for t in tokens:
            if t in "+/-*":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if t == '+':
                    stack.append(op1+op2)
                elif t == '-':
                    stack.append(op2-op1)
                elif t == '/':
                    stack.append(int(op2/op1)) # truncates towards 0
                elif t == '*':
                    stack.append(op1*op2)
            else:
                stack.append(t)
        
        print(stack)
        return int(stack[0])