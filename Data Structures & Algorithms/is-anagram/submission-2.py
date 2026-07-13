class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}

        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
        
        for j in t:
            if j in hashmap:
                hashmap[j]=hashmap[j]-1
            if j not in hashmap:
                return False
        
        for i in hashmap:
            if hashmap[i]!=0:
                return False
        
        return True
        