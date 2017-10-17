'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x:x.start)
        stack = []
        results = []
        for interval in intervals:
            if stack:
                if interval.start <= stack[-1]:
                    end = stack.pop()
                    stack.append(max(end, interval.end))
                else:
                    end = stack.pop()
                    start = stack.pop()
                    results.append([start, end])
                    stack.append(interval.start)
                    stack.append(interval.end)
            else:
                stack.append(interval.start)
                stack.append(interval.end)
        if stack:
            end = stack.pop()
            start = stack.pop()
            results.append([start, end])
        return results
