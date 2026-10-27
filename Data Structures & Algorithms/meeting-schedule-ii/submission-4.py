"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        meeting = []
        for interval in  intervals:
            meeting.append((interval.start,1))
            meeting.append((interval.end,-1))
        meeting.sort()

        room = 0
        cur = 0
        for time,val in meeting:
            cur += val
            room = max(room,cur)
        
        return room
            