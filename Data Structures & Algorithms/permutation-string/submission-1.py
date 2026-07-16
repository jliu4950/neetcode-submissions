class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        dic1={chr(ord('a')+i):0 for i in range(26)}
        dic2={chr(ord('a')+i):0 for i in range(26)}

        for i in range(len(s1)):
            dic1[s1[i]]+=1
            dic2[s2[i]]+=1

        #初始化match
        match=0
        for i in range(26):
            c=chr(ord("a")+i)
            if dic1[c]==dic2[c]:
                match+=1
        
        if match == 26:
            return True
        
        #固定窗口滑动
        for i in range(len(s1),len(s2)):
            
            dic2[s2[i]]+=1
            if dic2[s2[i]]==dic1[s2[i]]:
                match+=1
            elif dic2[s2[i]]==dic1[s2[i]]+1: #不用 > ，否则会match -=1 多次
                match-=1
            
            delete=i-len(s1)
            dic2[s2[delete]]-=1
            if dic2[s2[delete]]==dic1[s2[delete]]:
                match+=1
            elif dic2[s2[delete]]==dic1[s2[delete]]-1:
                match-=1

            if match==26:
                return True  
        
        return False
        