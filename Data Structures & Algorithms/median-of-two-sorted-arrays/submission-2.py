class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1)// 2
        if_odd = (m + n) % 2
        
        l = 0
        r = m

        while l <= r:
            i = (r - l) // 2 + l
            j = half - i

            #print(i,m)
            L1 = nums1[i - 1] if i > 0 else float("-inf")
            R1 = nums1[i] if i <len(nums1) else float("inf")
            L2 = nums2[j - 1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < len(nums2) else float("inf")

            if L1 > R2:
                r = i - 1
            elif L2 > R1:
                l = i + 1
            else:
                if if_odd == 1:
                    return max(L1,L2)
                else:
                    return (max(L1,L2) + min(R1,R2)) / 2
            