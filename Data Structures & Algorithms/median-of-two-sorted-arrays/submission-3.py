class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        lo = 0
        hi = m # left close，right close

        while lo <= hi:
            i = (hi - lo) // 2 + lo
            j = left - i
            L1 = nums1[i - 1] if i > 0 else float("-inf")
            R1 = nums1[i] if i < m else float("inf")
            L2 = nums2[j - 1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < n else float("inf")

            if L1 > R2:
                hi = i - 1
            elif L2 > R1:
                lo = i + 1
            else:
                if (m + n) % 2 == 1:
                    return max(L1,L2)
                else:
                    return (max(L1,L2) + min(R1,R2)) / 2

        '''
        if I merge two arrays,
        [0,1,2,3,4] 
              i
        odd : (n + 1) // 2 left has three

        [0,1,2,3]
             i
        even : (n + 1) // 2 left has two
        # i = 左边的个数 = 切口位置 = 右边第一个数的下标

        -> make sure left has (n + 1)// 2 elements
        
        if I don't merge nums1 and nums2

        nums1:[a,c,f...k,j] length = m
                    i
                    L1 = nums1[i - 1]
                    R1 = nums1[i]
        nums2:[k,c,a...a,d,e,f] length = n
                        j
                        L2 = nums2[j - 1]
                        R2 = nums2[j]
        i + j == (m + n + 1) // 2 
        -> I only need move i ,and j = (m + n + 1) // 2  - i
        1. choose which nums?
            choose shorter one -> not out of boundary
        2. how to move i?
            if L1 > R2:i move to left -> hi = i - 1
            if L2 > R1:i move to right -> lo = i + 1
            else: find
        3. when i = 0 or i = m/ j = 0 or j = n?
            use -inf and inf
        3. time : O(log(min(m,n)))
            space : O(1)
        
        '''