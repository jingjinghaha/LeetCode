'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
'''
# early stop
# once the there is out degree, skip the people
# only if the out degree is 0, keep tracking the in degree

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 1:
            return -1
        indegree = [0] * n
        outdegree = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and knows(i, j):
                    outdegree[i] += 1
                    break
            if outdegree[i] == 0:
                for j in range(n):
                    if i != j and knows(j, i):
                        indegree[i] += 1
                if indegree[i] == n-1:
                    return i
        return -1

# more tricky
# jump to find the candidate
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 1:
            return -1
        cur = 0
        for i in range(1, n):
            if knows(cur, i):
                cur = i
        for i in range(n):
            if i != cur and (not knows(i, cur) or knows(cur, i)):
                return -1
        return cur
