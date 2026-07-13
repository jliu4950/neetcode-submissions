class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i,num in enumerate(nums):
            arr.append((num,i))
        
        arr.sort(key=lambda x:x[0])

        l=0
        r=len(arr)-1

        while l<r:
            if arr[l][0]+arr[r][0]==target:
                return [min(arr[l][1],arr[r][1]),max(arr[l][1],arr[r][1])] 
            elif arr[l][0]+arr[r][0]<target:
                l+=1
            elif arr[l][0]+arr[r][0]>target:
                r-=1
        