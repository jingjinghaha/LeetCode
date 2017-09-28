'''
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
'''
# TLE
# O(n^2)
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        tmp = []  # in [i,j] intervals 
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in dict:
                    tmp.append([i, j+1])
         
        tt = [0]*(len(s)+1)
        for pos in tmp:
            tt[pos[0]] += 1
            tt[pos[1]] -= 1
        
        status = 0
        found = 0
        left = 0
        ans = ""
        for i in range(len(s)+1):
            status += tt[i]
            # found the start point to add <b>
            if status> 0 and found ==0:
                left = i
                found = 1
            # found the end point to add </b>
            if status ==0 and found ==1:
                found = 0
                ans+="<b>"+s[left:i]+"</b>"
            # not part of anu found term 
            if status ==0 and found ==0 and i < len(s):
                ans+= s[i]
        return ans

# O(n*m)
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bold = [0] * len(s)
        end = 0
        for i in range(len(s)):
            for word in dict:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            if end > i:
                bold[i] = 1
        print bold
        ans = ""
        i = 0
        while i < len(s):
            if bold[i] == 1:
                j = i
                while j < len(s) and bold[j] == 1:
                    j += 1
                ans += '<b>' + s[i:j] + '</b>'
                i = j
            else:
                ans += s[i]
                i += 1
        return ans

