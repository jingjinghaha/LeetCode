'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''
# two hashmap + two pointers
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        hash_t = {}
        for i in range(len(t)):
            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] += 1
        min_s = ""
        min_len = sys.maxint
        left = 0
        while left < len(s) and s[left] not in hash_t:
            left += 1
        right = left
        hash_s = {}
        while right < len(s):
            if s[right] in hash_t:
                if s[right] not in hash_s:
                    hash_s[s[right]] = 1
                else:
                    hash_s[s[right]] += 1
                while self.check(hash_s, hash_t):
                    length = right - left + 1
                    if length < min_len:
                        min_len = length
                        min_s = s[left:right+1]
                    hash_s[s[left]] -= 1
                    left += 1
                    while left < len(s) and s[left] not in hash_t:
                        left += 1
            right += 1
        return min_s
    
    def check(self, hash_s, hash_t):
        if len(hash_s) != len(hash_t):
            return False
        for key in hash_s:
            if hash_s[key] < hash_t[key]:
                return False
        return True

# one hashmap + two pointers
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
        table = self.build_hash(t)
        cnt = len(table)
        left = right = 0
        d = sys.maxint
        ans = ""
        while right < len(s):
            if s[right] in table:
                table[s[right]] -= 1
                if table[s[right]] == 0:
                    cnt -= 1
                while cnt == 0:
                    dis = right - left + 1
                    if dis < d:
                        d = dis
                        ans = s[left:right+1]
                    if s[left] in table:
                        table[s[left]] += 1
                        if table[s[left]] > 0:
                            cnt += 1
                    left += 1
            right += 1
        return ans
    
    def build_hash(self, t):
        hash_ = {}
        for i in range(len(t)):
            if t[i] not in hash_:
                hash_[t[i]] = 1
            else:
                hash_[t[i]] += 1
        return hash_

