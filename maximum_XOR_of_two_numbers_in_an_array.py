'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 ^ 25 = 28.
'''
class TrieNode():
    def __init__(self):
        self.children = {}
        
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return 0
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                curBit = (num >> i) & 1
                if curBit not in node.children:
                    node.children[curBit] = TrieNode()
                node = node.children[curBit]
                
        max_xor = -sys.maxint
        for num in nums:
            node = root
            curSum = 0
            for i in range(31, -1, -1):
                curBit = (num >> i) & 1
                if curBit ^ 1 in node.children:
                    curSum += (1 << i)
                    node = node.children[curBit ^ 1]
                else:
                    node = node.children[curBit]
            max_xor = max(max_xor, curSum)
        return max_xor
