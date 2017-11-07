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

# more tricky
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n):
            if s[i] != '0':
                dp[i] = 1
            else:
                dp[i] = 0
        for i in range(n - 2, -1, -1):
            if dp[i] == 0:
                continue
            else:
                if s[i:i+2] <= '26':
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
        return dp[0]


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
# DFS, TLE
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.helper(s, 0, '')
    def helper(self, s, start, tmp):
        if start == len(s):
            return 1
        if s[start] == '0':
            return 0
        cnt = 0
        if s[start] in '123456789':
            cnt += self.helper(s, start + 1, tmp + s[start])
        if s[start] == '1' and start < len(s) - 1:
            if s[start + 1] != '*':
                cnt += self.helper(s, start + 2, tmp + s[start: start+2])
            else:
                for i in range(9):
                    cnt += self.helper(s, start + 2, tmp + s[start] + str(i))
        if s[start] == '2' and start < len(s) - 1:
            if s[start + 1] != '*' and s[start + 1] <= '6':
                cnt += self.helper(s, start + 2, tmp + s[start: start+2])
            elif s[start + 1] == '*':
                for i in range(6):
                    cnt += self.helper(s, start + 2, tmp + s[start] + str(i))
        if s[start] == '*':
            for i in range(9):
                cnt += self.helper(s, start + 1, tmp + str(i))
            if start < len(s) - 1:
                if '0' <= s[start + 1] <= '9':
                    cnt += self.helper(s, start + 2, tmp + '1' + s[start + 1])
                if '0' <= s[start + 1] <= '6':
                    cnt += self.helper(s, start + 2, tmp + '2' + s[start + 1])
                if s[start + 1] == '*':
                    for i in range(11, 20):
                        cnt += self.helper(s, start + 2, tmp + str(i))
                    for i in range(21, 27):
                        cnt += self.helper(s, start + 2, tmp + str(i))    
        return cnt

# DP
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 1000000007
        if not s:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] == '0':
            return 0
        elif s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1
        for i in range(1, len(s)):
            if s[i] == '*':
                dp[i+1] = 9 * dp[i] % MOD
                if s[i-1] == '1':
                    dp[i+1] += 9 * dp[i-1] % MOD
                elif s[i-1] == '2':
                    dp[i+1] += 6 * dp[i-1] % MOD
                elif s[i-1] == '*':
                    dp[i+1] += 15 * dp[i-1] % MOD
            else:
                if s[i] == '0':
                    dp[i+1] = 0
                else:
                    dp[i+1] = dp[i] % MOD
                if s[i-1] == '1':
                    dp[i+1] += dp[i-1] % MOD
                elif s[i-1] == '2':
                    if '0' <= s[i] <= '6':
                        dp[i+1] += dp[i-1] % MOD
                elif s[i-1] == '*':
                    dp[i+1] += dp[i-1] % MOD
                    if '0' <= s[i] <= '6':
                        dp[i+1] += dp[i-1] % MOD
        return dp[-1] % MOD

# more tricky
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 1000000007
        e0 = 1
        e1 = 0
        e2 = 0
        for c in s:
            if c == '*':
                f0 = 9 * e0 + 9 * e1 + 6 * e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c != '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0 = f0 % MOD
            e1 = f1
            e2 = f2
        return e0

