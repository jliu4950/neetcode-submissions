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
        intervals.sort(key = lambda x: x.start)
        hp = []

        for interval in intervals:
            start = interval.start
            end = interval.end
            if hp and hp[0] <= start:
                heapq.heappop(hp)
            # if not hp:
            #     heapq.heappush(end)
            # elif hp[0] <= start:
            #     heapq.heappop(hp)
            #     heapq.heappush(hp,end)
            # else:
            heapq.heappush(hp,end)
        
        return len(hp)