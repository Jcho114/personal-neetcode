from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []

        for position, speed in cars:
            eta = (target-position)/speed
            while stack and eta >= stack[-1]:
                stack.pop()
            stack.append(eta)

        return len(stack)