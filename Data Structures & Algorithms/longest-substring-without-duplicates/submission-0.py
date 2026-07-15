class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        res=0
        l=0
        r=0
        while r<len(s):
            dic[s[r]]=dic.get(s[r],0)+1
            while dic[s[r]]>1:
                dic[s[l]]-=1
                l+=1
            r+=1
            res=max(r-l,res)
        return res
        