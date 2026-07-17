class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        need={}
        have={}
        for c in t:
            need[c]=need.get(c,0)+1
            if c not in have:
                have[c]=have.get(c,0)
        
        l=0
        match=0
        res=[-1,-1]
        length=float("inf")

        for r in range(len(s)):
            add=s[r]
            have[add]=have.get(add,0)+1
            if add in need and have[add]==need[add]:
                match+=1
            
            while match==len(need):
                if r-l+1<length:
                    res[0]=l
                    res[1]=r
                    length=r-l+1
                
                #delete left char
                d=s[l]
                have[d]-=1
                if d in need and have[d]<need[d]:
                    match-=1
                l+=1
        print(res)
        print(length)
        if length==float("inf"):
            return ""
        else:
            return s[res[0]:res[1]+1] 