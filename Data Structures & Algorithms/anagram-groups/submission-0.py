class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={} #sort:[groupAnagrams]

        for s in strs:
            t="".join(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t]=[s]

        #print(d)

        res=[]
        for item in d.values():
            res.append(item)
        
        return res
        