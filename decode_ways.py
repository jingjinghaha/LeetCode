'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
# DFS, TLE
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return self.helper(s)
    
    def helper(self, s):
        if not s:
            return 1
        count = 0
        if s[0] != '0':
            if len(s) >= 2 and s[:2] <= '26':
                count += self.helper(s[2:])
            count += self.helper(s[1:])
        return count

# DP
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [1] * len(s)
        if s[:2] <= '26' and s[1] != '0':
            dp[1] = 2
        if s[:2] > '26' and s[1] == '0':
            return 0
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i-1] > '2' or s[i-1] == '0':
                    return 0
                else:
                    dp[i] = dp[i-2]
            elif s[i-1:i+1] <= '26' and s[i-1] != '0':
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


'''
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 10^5].
The input string will only contain the character '*' and digits '0' - '9'.
'''

