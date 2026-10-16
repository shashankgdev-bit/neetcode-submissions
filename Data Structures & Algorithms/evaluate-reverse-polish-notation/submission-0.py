class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        maths = ['+', '-', '*', '/']

        for ch in tokens:
            if ch in maths:
                if ch == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)

                elif ch == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)

                elif ch == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)

                elif ch == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
            
            else:
                stack.append(int(ch))

        return stack.pop()

        