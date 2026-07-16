class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        l=0
        max_freq=0
        res=0

        for r in range(len(s)):
            dic[s[r]]+=1
            max_freq=max(dic[s[r]],max_freq)
            #print(max_freq)
            while r-l+1-max_freq>k:
                dic[s[l]]-=1
                l+=1
                max_freq=max(dic[s[l]],max_freq)
            
            res=max(res,r-l+1)
        
        return res
        