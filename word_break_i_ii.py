'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
# O(m*n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in xrange(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1: i+1] and (d[i-len(w)]==True or i ==len(w)-1):
                    d[i] = True
        return d[-1]


'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''
# DFS, TLE as there are a lot duplicated branches, have to use a hash map to prune these duplicated branches
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        results = []
        self.helper(s, wordDict, 0, "", results)
        return results
    
    def helper(self, s, words, start, tmp, results):
        if start == len(s):
            results.append(tmp)
        for i in range(start, len(s)):
            if s[start:i+1] in words:
                if start == 0:
                    self.helper(s, words, i+1, s[start:i+1], results)
                else:
                    self.helper(s, words, i+1, tmp + ' ' + s[start:i+1], results)

# memorized DFS
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mapping = {}
        return self.helper(s, wordDict, 0, mapping)
    
    def helper(self, s, words, start, mapping):
        if start in mapping:
            return mapping[start]
        ans = []
        for i in range(start, len(s)):
            if s[start:i+1] in words:
                if i == len(s) - 1:
                    ans.append(s[start:i+1])
                    break
                tmp = self.helper(s, words, i+1, mapping)
                for ss in tmp:
                    ans.append(s[start:i+1] + ' ' + ss)
        mapping[start] = ans
        return ans

