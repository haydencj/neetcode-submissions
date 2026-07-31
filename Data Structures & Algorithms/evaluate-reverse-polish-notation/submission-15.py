class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operands = {"+", "-", "*", "/"}
        if len(tokens) == 1:
            return int(tokens[0])

        for c in tokens:                
            if c in operands:
                op1 = stack.pop()
                op2 = stack.pop()
                if c == "+":
                    res = op1 + op2
                elif c == "-":
                    res = op2 - op1
                elif c == "*":
                    res = op1 * op2
                elif c == "/":
                    quotient = op2 / op1
                    res = int(quotient) # drops decimal aka truncates towards zero
                print(res)
                stack.append(res)
            else: stack.append(int(c))
        
        return res