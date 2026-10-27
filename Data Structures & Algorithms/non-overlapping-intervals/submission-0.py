class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # choose more intervals that not overlapp
        intervals.sort()
        res = 0 # how many intervals need to be remove
        preEnd = intervals[0][1]
        # print(intervals)

        for start,end in intervals[1:]:
            if preEnd <= start:
                preEnd = end
            else:
                res += 1
                preEnd = min(preEnd,end)
        
        return res

        