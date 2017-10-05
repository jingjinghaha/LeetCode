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


