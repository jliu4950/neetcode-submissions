from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int) # val -> idx
        l = 0
        res = 0

        for r,char in enumerate(s):
            if char in dic:
                l = max(l,dic[char] + 1)
            
            dic[char] = r
            res = max(r - l + 1,res)
        
        return res
        