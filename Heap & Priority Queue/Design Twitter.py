from typing import List
from collections import defaultdict
import heapq

class User:
    def __init__(self):
        self.tweets = []
        self.followees = set()

class Twitter:
    def __init__(self):
        self.users = defaultdict(User)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweets.append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        TC: O(nlogk)
        SC: O(n)
        """
        heap = []
        self.users[userId].followees.add(userId)
        for followeeId in self.users[userId].followees:
            for count, tweetId in self.users[followeeId].tweets:
                heapq.heappush(heap, (count, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)

        res = []
        while heap:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].followees.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId].followees:
            self.users[followerId].followees.remove(followeeId)