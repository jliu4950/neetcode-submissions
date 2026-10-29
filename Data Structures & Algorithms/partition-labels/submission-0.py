class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        
        for i,c in enumerate(s):
            if c not in dic:
                dic[c] = [i,i]
            else:
                dic[c][1] = i
        
        intervals = [[l,r] for l,r in dic.values()]

        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            l , r = intervals[i]
            if end > l:
                end = max(r,end)
            else:
                res.append(end - start + 1)
                start = l
                end = r
        
        res.append(end - start + 1)
        return res