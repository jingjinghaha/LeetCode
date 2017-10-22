'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        mapping = {'(':')','[':']','{':'}'}
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] in '({[' and s[i] == mapping[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[i])
        if stack == []:
            return True
        return False
