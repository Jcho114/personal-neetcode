class WordDictionary:
    def __init__(self):
        self.delim  ="$"
        self.wildcard = "."
        self.root = {}        

    def addWord(self, word: str) -> None:
        """
        TC: O(m)
        SC: O(m)
        """
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr[self.delim] = {}

    def search(self, word: str) -> bool:
        """
        TC: O(m)
        SC: O(m)
        """
        def helper(curr: dict, i: int) -> bool:
            if i == len(word):
                return self.delim in curr
            c = word[i]
            if c == self.wildcard:
                return any(helper(child, i+1) for child in curr.values())
            if c not in curr:
                return False
            return helper(curr[c], i+1)

        return helper(self.root, 0)