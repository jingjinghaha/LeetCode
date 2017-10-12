'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''
# hash table + queue
# time: O(n)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_hash = {}
        for i in range(len(tasks)):
            if tasks[i] not in task_hash:
                task_hash[tasks[i]] = 1
            else:
                task_hash[tasks[i]] += 1
        task_freq = sorted(task_hash.iteritems(), key = lambda x:x[1], reverse = True)
        from collections import deque
        q = deque()
        for item in task_freq:
            q.append(list(item))
        ans = 0
        print q
        while len(q):
            size = len(q)
            cnt = 0
            del_list = []
            for i in range(size):
                q[i][1] -= 1
                ans += 1
                cnt += 1
                if cnt == n + 1:
                    break
            while q[0][1] != 0 and cnt < n + 1:
                cnt += 1
                ans += 1
            for i in range(size-1, -1, -1):
                if q[i][1] == 0:
                    del q[i]
            q = sorted(q, key = lambda x:x[1],reverse = True)
        return ans

# more tricky
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_hash = {}
        for i in range(len(tasks)):
            if tasks[i] not in task_hash:
                task_hash[tasks[i]] = 1
            else:
                task_hash[tasks[i]] += 1
        task_freq = sorted(task_hash.iteritems(), key = lambda x:x[1], reverse = True)
        cnt = 0
        for item in task_freq:
            if item[1] == task_freq[0][1]:
                cnt += 1
            else:
                break
        return max(len(tasks), (task_freq[0][1] - 1)*(n + 1) + cnt)

