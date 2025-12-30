from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        operators = "+-*/"
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                v2, v1 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(v1 + v2)
                elif token == "-":
                    stack.append(v1 - v2)
                elif token == "*":
                    stack.append(v1 * v2)
                elif token == "/":
                    stack.append(int(v1 / v2))

        return stack[-1]