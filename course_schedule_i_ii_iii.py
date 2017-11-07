'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
# BFS, this also works for course schedule II
# this problem is relatively easy, just to judge if there is a cycle 
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses or not prerequisites:
            return True
        adjacency = self.gene_adjacency(numCourses, prerequisites)
        in_degree = self.in_degree(numCourses, prerequisites)
        from collections import deque
        q = deque()
        schedule = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
                schedule.append(course)
        print adjacency,in_degree,q
        while q:
            course = q.popleft()
            for next in adjacency[course]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    q.append(next)
                    schedule.append(next)
        if len(schedule) == numCourses:
            return True
        return False
    
    def gene_adjacency(self, num, prerequisites):
        adjacency = []
        for i in range(num):
            adjacency.append([])
        for pair in prerequisites:
            adjacency[pair[0]].append(pair[1])
        return adjacency
    
    def in_degree(self, num, prerequisites):
        in_degree = [0] * num
        for pair in prerequisites:
            in_degree[pair[1]] += 1
        return in_degree

# DFS, which is much faster than BFS in this case
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacent = self.adjacent_matrix(numCourses, prerequisites)
        visited = [False] * numCourses
        path = [False] * numCourses
        for i in range(numCourses):
            if not visited[i] and self.dfs(adjacent, i, path, visited):
                return False
        return True
        
    def adjacent_matrix(self, num, pre):
        adjacent = []
        for i in range(num):
            adjacent.append([])
        for pair in pre:
            adjacent[pair[1]].append(pair[0])
        return adjacent
    
    def dfs(self, adj, cur, path, visited):
        if visited[cur]:
            return False
        visited[cur] = True
        path[cur] = True
        for next in adj[cur]:
            if path[next] or self.dfs(adj, next, path, visited):
                return True
        path[cur] = False
        return False

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []
        adjacency = self.gene_adjacency(numCourses, prerequisites)
        in_degree = self.in_degree(numCourses, prerequisites)
        from collections import deque
        q = deque()
        schedule = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
                schedule.append(course)
        print adjacency,in_degree,q
        while q:
            course = q.popleft()
            for next in adjacency[course]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    q.append(next)
                    schedule.append(next)
        if len(schedule) == numCourses:
            return schedule
        return []
    
    def gene_adjacency(self, num, prerequisites):
        adjacency = []
        for i in range(num):
            adjacency.append([])
        for pair in prerequisites:
            adjacency[pair[1]].append(pair[0])
        return adjacency
    
    def in_degree(self, num, prerequisites):
        in_degree = [0] * num
        for pair in prerequisites:
            in_degree[pair[0]] += 1
        return in_degree

# DFS 
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacent = self.adjacent_matrix(numCourses, prerequisites)
        visited = [False] * numCourses
        path = [False] * numCourses
        order = []
        for i in range(numCourses):
            if not visited[i] and self.dfs(adjacent, i, path, visited, order):
                return []
        order.reverse()
        return order
        
    def adjacent_matrix(self, num, pre):
        adjacent = []
        for i in range(num):
            adjacent.append([])
        for pair in pre:
            adjacent[pair[1]].append(pair[0])
        return adjacent
    
    def dfs(self, adj, cur, path, visited, order):
        if visited[cur]:
            return False
        visited[cur] = True
        path[cur] = True
        for next in adj[cur]:
            if path[next] or self.dfs(adj, next, path, visited, order):
                return True
        path[cur] = False
        order.append(cur)
        return False

'''
There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
'''

