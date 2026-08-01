from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # user :[(post_time,tid)]
        self.followers = defaultdict(set)
        self.post_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.post_time,tweetId))
        self.post_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followers[userId] | {userId}

        hp = []
        for u_id in users:
            if self.tweets[u_id]:
                p_time,t_id = self.tweets[u_id][-1]
                hp.append((-p_time,u_id,t_id,len(self.tweets[u_id])-1))
        
        heapq.heapify(hp)

        res=[]
        i = 0
        while i<10 and hp:
            p_time,u_id,t_id,idx = heapq.heappop(hp)
            res.append(t_id)
            if idx > 0:
                nxt_idx = idx - 1
                next_ptime ,next_tid = self.tweets[u_id][nxt_idx]
                heapq.heappush(hp,(-next_ptime , u_id , next_tid ,nxt_idx))
            i+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)