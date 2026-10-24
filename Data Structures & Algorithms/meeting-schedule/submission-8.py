"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if len(intervals)==1 or len(intervals)==0:
            return True
        elif len(intervals)==2:
            if intervals[0].end<=intervals[1].start:
                return True
            else:
                return False
        else:
            return self.canAttendMeetings(intervals[:2]) and self.canAttendMeetings(intervals[1:]) 
