'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key = lambda x:x.start)
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                return False
            end = intervals[i].end
        return True

'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# sort + heap
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        def cmp(x, y):
            return x.start - y.start
        intervals.sort(cmp)
        import heapq
        heap = []
        min_room = 0
        for i in range(len(intervals)):
            while heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            min_room = max(min_room, len(heap))
        return min_room

# initial solution, put both start time and end time to a time schedule list
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        START = 2
        END = 1
        def cmp_function(x, y):
            if x[0] == y[0]:
                return x[1] - y[1]
            return x[0] - y[0]
        schedule = []
        for interval in intervals:
            schedule.append([interval.start, START])
            schedule.append([interval.end, END])
        schedule.sort(cmp_function)
        
        room = 0
        tmp_room = 0
        for time in schedule:
            if time[1] == START:
                tmp_room += 1
            if time[1] == END:
                tmp_room -= 1
            if tmp_room > room:
                room = tmp_room
        return room

# more tricky
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        starts = []
        ends = []
        for interval in intervals:
            print interval.start, interval.end
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        rooms = 0
        end_idx = 0
        for i in range(len(starts)):
            if starts[i] < ends[end_idx]:
                rooms += 1
            else:
                end_idx += 1
        return rooms
