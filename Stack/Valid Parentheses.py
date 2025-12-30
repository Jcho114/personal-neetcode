class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        stack = []
        pairing = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c not in pairing:
                stack.append(c)
            else:
                if len(stack) == 0 or pairing[c] != stack.pop():
                    return False

        return len(stack) == 0