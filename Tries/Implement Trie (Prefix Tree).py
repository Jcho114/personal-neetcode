class Trie:
    def __init__(self):
        self.delimiter = "$"
        self.root = {}

    def insert(self, word: str) -> None:
        """
        TC: O(m)
        SC: O(m)
        """
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr[self.delimiter] = {}

    def search(self, word: str) -> bool:
        """
        TC: O(m)
        SC: O(1)
        """
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return self.delimiter in curr

    def startsWith(self, prefix: str) -> bool:
        """
        TC: O(m)
        SC: O(1)
        """
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True