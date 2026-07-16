class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        dic_t={}
        for c in t:
            dic_t[c]=dic_t.get(c,0)+1
        
        l=0
        res=[]
        window={}
        need=0

        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            if s[r] in dic_t and window[s[r]]==dic_t[s[r]]:  # 如果 s[r] 不在 dic_t 中会 KeyError
                need+=1
            while need==len(dic_t): 
                res.append((l,r+1)) #记录所有合法窗口
                #不断缩小左窗口
                if s[l] in dic_t:
                    if window[s[l]]==dic_t[s[l]]:
                        need-=1
                    window[s[l]]-=1
                l+=1
        
        res.sort(key = lambda x: x[1]-x[0])
        
        return s[res[0][0]:res[0][1]] if res else ""
        