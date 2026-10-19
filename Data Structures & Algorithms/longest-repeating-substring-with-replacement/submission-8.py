from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        window: 
            dic : char -> freq
            记录出现最多次数的char的频次 max_freq
        expand:
            update max_freq
        shrink:
            if len(window) - max_freq > k:
                delete left 
                update max_freq
        update length
        '''
        dic = defaultdict(int)
        max_freq = 0
        res = 0
        l = 0

        for r,c in enumerate(s):
            dic[c] += 1
            max_freq = max(max_freq, dic[c])
            while r - l + 1 - max_freq > k:
                dic[s[l]] -= 1
                l += 1
            
            res = max(res,r - l + 1)
        
        return res