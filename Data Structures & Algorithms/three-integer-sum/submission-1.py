class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        print(nums)

        i=0

        while i<len(nums):
            while i>0 and i <len(nums) and nums[i]==nums[i-1]:
                i+=1
            #print(i)
            j=i+1 
            k=len(nums)-1
            while j<k:
                total=nums[j]+nums[k]+nums[i]
                # print(f"i:{i},j:{j},k:{k},total:{total}")
                # print(f"i:{nums[i]},j:{nums[j]},k:{nums[k]}")

                if total==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    #找到正确答案后，把j,k重复值去掉
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif total<0:
                    j+=1
                elif total>0:
                    k-=1

            i+=1
        return res