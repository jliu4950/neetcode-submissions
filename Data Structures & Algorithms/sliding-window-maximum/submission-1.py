class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=k:
            return [max(nums)]
        
        res=[]

        w=[0]
        
        for i in range(1,k):
            while w and nums[w[-1]]<=nums[i]:
                w.pop()
            w.append(i)
        res.append(nums[w[0]])
        
        l=0
        for r in range(k,len(nums)):
            a=[]
            for i in w:
                a.append(nums[i])
            print(w)
            print(a)
            #add
            while w and nums[w[-1]]<=nums[r]:
                w.pop()
            w.append(r)
            #delete
            if w[0]<=l:
                w=w[1:]
            l+=1
            
            #record
            res.append(nums[w[0]])
        
        return res