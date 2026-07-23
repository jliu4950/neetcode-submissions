# 重复说明两个pos指向该位置，找环相交点

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow] #slow step 1
            fast = nums[nums[fast]] #fast step 2
            if slow==fast:
                break
        
        slow2 = 0
        while True:
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]
         