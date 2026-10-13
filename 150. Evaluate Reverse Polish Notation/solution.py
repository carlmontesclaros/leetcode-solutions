class Solution:

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        s = set("+-*/")

        for token in tokens:
            if token not in s:
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if token == "+":
                    stack.append(n2+n1)
                elif token == "-":
                    stack.append(n2-n1)
                elif token == "*":
                    stack.append(n2*n1)
                else:
                    stack.append(int(n2/n1))

        return stack[-1]