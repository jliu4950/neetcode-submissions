class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1.
        3,4,5,6,1,2
                l
                r
                m
        2.
        1,2,3,4,5,6
        l
        r
        m
        '''

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m - 1
        
        return nums[l]
        