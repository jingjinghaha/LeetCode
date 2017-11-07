'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = []
        i = 0
        while i < len(s) and s[i] not in '+-*/':
            i += 1
        stack.append(int(s[:i]))
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] not in '+-*/':
                j += 1
            cur = int(s[i+1:j])
            if s[i] == '*':
                prev = stack.pop()
                cur *= prev
            if s[i] == '/':
                prev = stack.pop()
                if prev >= 0:
                    cur = prev / cur
                else:
                    cur = - (- prev / cur)
            if s[i] == '-':
                cur = -cur
            stack.append(cur)
            i = j
        return sum(stack)

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''

