'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''
# the first implementation passed the tests in Leetcode, but actually has some bugs, like it cannot detect '++3' as an invalid number which is actually invalid
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        s_number = ''
        indicator_e = False
        indicator_dot = False
        for i in range(len(s)):
            if not s[i].isalpha() and not s[i].isdigit() and s[i] not in '.+-':
                return False
            if s[i] in '+-':
                if s_number:
                    if s_number[-1] != 'e':
                        return False
                    s_number += s[i]
            if s[i].isalpha():
                if s[i] != 'e':
                    return False
                else:
                    if indicator_e == True:
                        return False
                    indicator_e = True
                    if not s_number or s_number == '.':
                        return False
                    s_number += s[i]
            if s[i] == '.':
                if indicator_dot == True or indicator_e == True:
                    return False
                indicator_dot = True
                s_number += s[i]
            if s[i].isdigit():
                s_number += s[i]
        if not s_number or s_number[-1] in 'e+-' or s_number == '.':
            return False
        return True

# the following new implementation is better than the previous one
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        indicator_e = False
        indicator_dot = False
        res = ''
        for i in range(len(s)):
            if s[i] not in '.e+-' and not s[i].isdigit():
                return False
            if s[i] in '+-':
                if not res:
                    res += s[i]
                elif res[-1] != 'e':
                    return False
                elif res[-1] == 'e':
                    res += s[i]
            elif s[i] == '.':
                if indicator_dot or indicator_e:
                    return False
                indicator_dot = True
                res += '.'
            elif s[i] == 'e':
                if indicator_e:
                    return False
                indicator_e = True
                if not res or res == '.' or res == '-' or res == '+':
                    return False
                res += 'e'
            else:
                res += s[i]
        if res[-1] in 'e+-' or res == '.' or res == '+.' or res == '-.':
            return False
        return True

