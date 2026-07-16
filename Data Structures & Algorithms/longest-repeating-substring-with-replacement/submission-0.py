class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        l=0
        max_freq=0
        res=0

        for r in range(len(s)):
            #when window-max_freq>k:shrink
            dic[s[r]]+=1

            for key,freq in dic.items():
                if freq>max_freq:
                    max_freq=freq

            while r-l+1-max_freq>k:
                dic[s[l]]-=1
                l+=1
                for key,freq in dic.items():
                    if freq>max_freq:
                        max_freq=freq

            res=max(res,r-l+1)
        
        return res
        