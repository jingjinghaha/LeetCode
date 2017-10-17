'''
Given two strings S and T, determine if they are both one edit distance apart.
'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False
        if abs(len(s) - len(t)) >= 2:
            return False
        i = 0
        j = 0
        diff = 0
        while i < len(s) or j < len(t):
            if i >= len(s):
                diff += 1
                j += 1
                continue
            if j >= len(t):
                diff += 1
                i += 1
                continue
            if s[i] != t[j]:
                diff += 1
                if diff >= 2:
                    return False
                if len(s) - i == len(t) - j:
                    i += 1
                    j += 1
                elif len(s) - i > len(t) - j:
                    i += 1
                else:
                    j += 1
            else:
                i += 1
                j += 1
        return diff == 1

# more tricky
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False
        if abs(len(s) - len(t)) >= 2:
            return False
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) > len(t):
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return abs(len(s) - len(t)) == 1

