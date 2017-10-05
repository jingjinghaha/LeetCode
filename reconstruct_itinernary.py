'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''
# recursively
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import bisect
        if not tickets:
            return []
        mapping = {}
        for pair in tickets:
            if pair[0] not in mapping:
                mapping[pair[0]] = [pair[1]]
            else:
                bisect.insort(mapping[pair[0]], pair[1])
        print mapping
        result = []
        self.dfs('JFK', result, mapping)
        result.reverse()
        return result
    
    def dfs(self, departure, result, mapping):
        import heapq
        while departure in mapping and mapping[departure] != []:
            self.dfs(heapq.heappop(mapping[departure]), result, mapping)
        result.append(departure)

# literately
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import bisect
        if not tickets:
            return []
        mapping = {}
        for pair in tickets:
            if pair[0] not in mapping:
                mapping[pair[0]] = [pair[1]]
            else:
                bisect.insort(mapping[pair[0]], pair[1])
            if pair[1] not in mapping:
                mapping[pair[1]] = []
        print mapping
        stack = ['JFK']
        schedule = []
        while stack:
            flight = stack[-1]
            if mapping[flight] == []:
                schedule.append(flight)
                stack.pop()
            else:
                stack.append(mapping[flight][0])
                del mapping[flight][0]
        schedule.reverse()
        return schedule
