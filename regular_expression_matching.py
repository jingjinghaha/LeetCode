'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''
# DFS
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not s:
            return self.checkp(p)
        if not p:
            return False
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                for i in range(len(s) + 1):
                    if self.isMatch(s[i:], p[2:]):
                        return True
            if s[0] != p[0]:
                if self.isMatch(s, p[2:]):
                    return True
            if s[0] == p[0]:
                for i in range(len(s) + 1):
                    if self.isMatch(s[i:], p[2:]):
                        return True
                    if i and i < len(s) and s[i] != s[i-1]:
                        break
        else:
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
        return False
    def checkp(self, p):
        if len(p) % 2 != 0:
            return False
        for i in range(len(p)):
            if i % 2 == 1 and p[i] != '*':
                return False
        return True

# memorized DFS
class Solution(object):
    mapping = {}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        key = s + '->' + p
        if key in self.mapping:
            return self.mapping[key]
        if not s and not p:
            return True
        if not s:
            return self.checkp(p)
        if not p:
            return False
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                for i in range(len(s) + 1):
                    if s[i:]+'->'+p[2:] in self.mapping:
                        is_match = self.mapping[s[i:]+'->'+p[2:]]
                    else:
                        is_match = self.isMatch(s[i:], p[2:])
                        self.mapping[s[i:]+'->'+p[2:]] = is_match
                    if is_match:
                        return True
            if s[0] != p[0]:
                if s+'->'+p[2:] in self.mapping:
                    is_match = self.mapping[s+'->'+p[2:]]
                else:
                    is_match = self.isMatch(s, p[2:])
                    self.mapping[s+'->'+p[2:]] = is_match
                if is_match:
                    return True
            if s[0] == p[0]:
                for i in range(len(s) + 1):
                    if s[i:]+'->'+p[2:] in self.mapping:
                        is_match = self.mapping[s[i:]+'->'+p[2:]]
                    else:
                        is_match = self.isMatch(s[i:], p[2:])
                        self.mapping[s[i:]+'->'+p[2:]] = is_match
                    if is_match:
                        return True
                    if i and i < len(s) and s[i] != s[i-1]:
                        break
        else:
            if s[0] == p[0] or p[0] == '.':
                if s[1:]+'->'+p[1:] in self.mapping:
                    is_match = self.mapping[s[1:]+'->'+p[1:]]
                else:
                    is_match = self.isMatch(s[1:], p[1:])
                    self.mapping[s[1:]+'->'+p[1:]] = is_match
                return is_match
        return False
    def checkp(self, p):
        if len(p) % 2 != 0:
            return False
        for i in range(len(p)):
            if i % 2 == 1 and p[i] != '*':
                return False
        return True

