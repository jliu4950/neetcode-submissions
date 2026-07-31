from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.user_tweet = defaultdict(list) # userid : [(tweet,posttime),]
        self.follower = defaultdict(set) # userid:[ followerid ] #有可能会关注多次，去重
        self.posttime = 0
        self.hp = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId].append((self.posttime,tweetId))
        self.posttime +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = [(-posttime,tweetid) for posttime,tweetid in self.user_tweet[userId]]
        heapq.heapify(hp)

        newsFeed = []
        
        followlist = self.follower[userId]
        for followee in followlist:
            if followee == userId: # user 可能会关注自己
                continue
            for posttime,tweetid in self.user_tweet[followee]:
                heapq.heappush(hp,(-posttime,tweetid))

        i = 0
        while hp and i<10:
            time,tweetid = heapq.heappop(hp)
            newsFeed.append(tweetid)
            i+=1
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        #print(self.follower)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
