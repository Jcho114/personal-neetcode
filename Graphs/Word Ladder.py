from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        TC: O(m^2 * n)
        TC: O(m^2 * n)
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(L):
                patterns[word[:i] + '*' + word[i+1:]].append(word)

        queue = deque([(1, beginWord)])

        visited = set()
        while queue:
            dist, curr_word = queue.popleft()
            for i in range(L):
                inter = curr_word[:i] + '*' + curr_word[i+1:]
                for word in patterns[inter]:
                    if word == endWord:
                        return dist + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((dist+1, word))
                patterns[inter] = []

        return 0