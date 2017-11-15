'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
'''
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        sum = 0
        for nested in nestedList:
            if nested.isInteger():
                sum += nested.getInteger()
            else:
                sum += self.helper(nested, 2)
        return sum
    def helper(self, nested, depth):
        if not nested:
            return 0
        sum = 0
        for ele in nested.getList():
            if ele.isInteger():
                sum += ele.getInteger() * depth
            else:
                sum += self.helper(ele, depth + 1)
        return sum


'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
'''
# BFS 
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        weighted = 0
        unweighted = 0
        from collections import deque
        q = deque()
        for ele in nestedList:
            q.append(ele)
        while len(q):
            size = len(q)
            level_sum = 0
            for i in range(size):
                ele = q.popleft()
                if ele.isInteger():
                    level_sum += ele.getInteger()
                else:
                    for next in ele.getList():
                        q.append(next)
            unweighted += level_sum
            weighted += unweighted
        return weighted

