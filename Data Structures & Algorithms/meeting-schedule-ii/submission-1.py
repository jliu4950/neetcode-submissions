"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)

        hp = []

        for x in intervals:
            start = x.start
            end = x.end

            if not hp or hp[0] > start:
                heapq.heappush(hp,end)
            else:
                heapq.heappop(hp)
                heapq.heappush(hp,end)
        
        return len(hp)
                
        