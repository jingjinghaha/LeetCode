'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''
# memorized DFS
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        m, n = self.check_invalid_number(s)
        result = set()
        visited = set()
        self.helper(s, m, n, result, visited)
        return list(result)
    
    def helper(self, s, m, n, result, visited):
        if s in visited:
            return
        if m == 0 and n == 0:
            if s not in result and self.check_valide(s):
                result.add(s)
            return
        if m > 0:
            for i in range(len(s)):
                if s[i] == '(':
                    self.helper(s[:i]+s[i+1:], m-1, n, result, visited)
                    visited.add(s[:i]+s[i+1:])
        if n > 0:
            for i in range(len(s)):
                if s[i] == ')':
                    self.helper(s[:i]+s[i+1:], m, n-1, result, visited)
                    visited.add(s[:i]+s[i+1:])
    
    def check_invalid_number(self, s):
        stack = self.extract_parentheses(s)
        m = n = 0
        for ele in stack:
            if ele == '(':
                m += 1
            if ele == ')':
                n += 1
        return m, n
    
    def check_valide(self, s):
        stack = self.extract_parentheses(s)
        if len(stack):
            return False
        return True
    
    def extract_parentheses(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif s[i] in '()':
                stack.append(s[i])
        return stack


