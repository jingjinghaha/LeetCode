'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        cur = 1
        result = "1"
        while cur < n:
            i = 0
            tmp = ""
            while i < len(result):
                count = 1
                j = i
                while j < len(result) - 1 and result[j+1] == result[j]:
                    j += 1
                    count += 1
                tmp += str(count) + result[i]
                i = j + 1
            result = tmp
            cur += 1
        return result


