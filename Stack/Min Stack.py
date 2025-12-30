class MinStack:
    def __init__(self):
        """
        TC: O(1)
        SC: O(n)
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        TC: O(1)
        SC: O(1)
        """
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        """
        TC: O(1)
        SC: O(1)
        """
        self.stack.pop()

    def top(self) -> int:
        """
        TC: O(1)
        SC: O(1)
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        TC: O(1)
        SC: O(1)
        """
        return self.stack[-1][1]