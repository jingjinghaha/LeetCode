'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
'''
# BFS, TLE
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        from collections import deque
        q = deque()
        q.append(beginWord)
        step = 1
        while len(q):
            size = len(q)
            for i in range(size):
                currWord = q.popleft()
                for i in xrange(len(currWord)):
                    left = currWord[:i]
                    right = currWord[i+1:]
                    for v in "qwertyuiopasdfghjklzxcvbnm":
                        nextWord = left + v + right
                        if nextWord == endWord:
                            return step + 1
                        if nextWord in wordList:
                            q.append(nextWord)
                            wordList.remove(nextWord)
            step += 1
        return 0

# store the wordList to a dictionary, accepted finally, but this is not the best solution
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set()
        for word in wordList:
            words.add(word)
        if endWord not in words:
            return 0
        from collections import deque
        q = deque()
        q.append(beginWord)
        step = 1
        while len(q):
            size = len(q)
            for i in range(size):
                currWord = q.popleft()
                for i in xrange(len(currWord)):
                    left = currWord[:i]
                    right = currWord[i+1:]
                    for v in "qwertyuiopasdfghjklzxcvbnm":
                        nextWord = left + v + right
                        if nextWord == endWord:
                            return step + 1
                        if nextWord in words:
                            q.append(nextWord)
                            words.remove(nextWord)
            step += 1
        return 0

# two-end search solution: begin both from start and end. Once we meet the same word from start and end, we know we are done. 
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set()
        for word in wordList:
            words.add(word)
        if endWord not in words:
            return 0
        from collections import deque
        beginq = deque()
        beginq.append(beginWord)
        endq = deque()
        endq.append(endWord)
        step = 1
        while len(beginq) and len(endq):
            if len(endq) < len(beginq):
                tmp = beginq
                beginq = endq
                endq = tmp
            size = len(beginq)
            for i in range(size):
                currWord = beginq.popleft()
                for i in xrange(len(currWord)):
                    left = currWord[:i]
                    right = currWord[i+1:]
                    for v in "qwertyuiopasdfghjklzxcvbnm":
                        nextWord = left + v + right
                        if nextWord in endq:
                            return step + 1
                        if nextWord in words:
                            beginq.append(nextWord)
                            words.remove(nextWord)
            step += 1
        return 0

