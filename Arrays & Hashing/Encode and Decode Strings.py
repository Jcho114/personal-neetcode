from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        TC: O(n)
        SC: O(n)
        """
        parts = []
        for s in strs:
            part = f"{len(s)}#{s}"
            parts.append(part)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        """
        TC: O(n)
        SC: O(m)
        """
        i = 0
        parts = []
        while i < len(s):
            length = 0
            while s[i] != '#':
                length = length*10 + int(s[i])
                i += 1
            part = s[i+1:i+1+length]
            parts.append(part)
            i = i+1+length
        return parts