'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return None
        indicator = False
        s = list(str(num))
        for i in range(1, len(s)):
            if s[i] > s[i-1]:
                indicator = True
                break
        if indicator == False:
            return num
        idx = i + self.find_max(s[i:])
        for i in range (len(s)):
            if s[i] < s[idx]:
                tmp = s[i]
                s[i] = s[idx]
                s[idx] = tmp
                break
        return int(''.join(s))
    
    def find_max(self, s):
        max_value = s[0]
        pos = 0
        for i in range(1, len(s)):
            if s[i] >= max_value:
                max_value = s[i]
                pos = i
        return pos
