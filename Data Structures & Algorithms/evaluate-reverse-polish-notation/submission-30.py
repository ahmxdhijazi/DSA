class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        res = 0

        for token in tokens:
            if stack and (token in operators):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == "+":
                    res = num2 + num1
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num2 * num1
                elif token == "/":
                    res = 0 if num1 == 0 else int(float(num2) / num1)  # Truncate toward zero
                
                stack.append(res)

            else:
                stack.append(token)

        return int(stack.pop())

