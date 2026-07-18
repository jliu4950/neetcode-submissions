class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)
        m=(r-l)//2+l
        while l<r:
            print(f"l:{l},r:{r}")
            if target<nums[m]:
                r=m
            elif target>nums[m]:
                l=m+1
            else:
                return m
            
            m=(r-l)//2+l
        
        return -1
        