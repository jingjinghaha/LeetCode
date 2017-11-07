'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''
# DFS, TLE
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            if not s:
                return True
            return False
        if not s:
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True
        if p[0] == '*':
            i = 0
            while i < len(p) and p[i] == '*':
                i += 1
            if i == len(p):
                return True
            if p[i] != '?':
                for j in range(len(s)):
                    if s[j] == p[i]:
                        if self.isMatch(s[j+1:], p[i+1:]):
                            return True
            else:
                for j in range(len(s)):
                    if self.isMatch(s[j+1:], p[i+1:]):
                        return True
        else:
            if s[0] == p[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        return False


