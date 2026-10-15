from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        l = 0
        res = 0
        max_c = s[0]

        for r,char in enumerate(s):
            dic[char] += 1
            while r - l + 1 - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1
            
            res = max(res,r - l + 1)
        
        return res