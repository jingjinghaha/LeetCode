'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.helper(n, 0, 0, "", results)
        return results
    def helper(self, n, cnt1, cnt2, tmp, results):
        if len(tmp) == 2 * n:
            results.append(tmp)
            return
        if cnt1 < n:
            self.helper(n, cnt1+1, cnt2, tmp+"(", results)
        if cnt2 < cnt1:
            self.helper(n, cnt1, cnt2+1, tmp+")", results)
