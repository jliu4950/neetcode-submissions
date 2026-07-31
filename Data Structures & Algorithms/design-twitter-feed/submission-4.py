from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time_stamp , tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        users = set(self.followees[userId]) #必须加上set，不然直接就操作集合
        users.add(userId)

        res = []
        hp =  []
        for usid in users:
            tweets = self.user_tweets[usid]
            if not tweets:
                continue
            last_idx = len(tweets) - 1
            t,tid =tweets[last_idx]
            hp.append((-t, tid , usid ,last_idx))
        
        heapq.heapify(hp)

        while len(res) < 10 and hp:
            neg_t,tid,uid,idx = heapq.heappop(hp)
            res.append(tid)
            
            if idx > 0:
                nxt_t,nxt_tid = self.user_tweets[uid][idx - 1]
                heapq.heappush(hp,(-nxt_t , nxt_tid , uid, idx - 1))
        
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)