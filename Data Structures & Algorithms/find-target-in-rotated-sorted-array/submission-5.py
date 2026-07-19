class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        minVal=nums[r]
        start=0
        
        #find min
        while l<=r:
            m=(r-l)//2+l
            cur =nums[m]

            if cur>nums[r]:
                l=m+1
            elif cur<=nums[r]:
                r=m-1
                if cur<=minVal:
                    minVal=cur
                    start=m

        if start==0:
            l=0
            r=len(nums)-1
        elif target>nums[0]:
            l=0
            r=start-1
        elif target<nums[0]:
            l=start
            r=len(nums)-1
        elif target == nums[0]:
            return 0
        
        while l<=r:
            m=(r-l)//2+l
            cur=nums[m]
            if cur==target:
                return m
            elif cur>target:
                r=m-1
            elif cur<target:
                l=m+1
        
        return -1