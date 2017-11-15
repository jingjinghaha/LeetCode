'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
# my initial idea is to use hashmap to store the idx of each word, but the following solution is more brief and more efficient for one call
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = sys.maxint
        p1 = -1
        p2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                dis = min(dis, abs(p1 - p2))
        return dis


'''
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
# for multiple calls, using hashmap is better
class WordDistance(object):
    hashmap = {}
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hashmap = {}
        for i in range(len(words)):
            if words[i] not in self.hashmap:
                self.hashmap[words[i]] = []
            self.hashmap[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = self.hashmap[word1]
        pos2 = self.hashmap[word2]
        i = 0
        j = 0
        dis = sys.maxint
        while i < len(pos1) and j < len(pos2):
            diff = pos1[i] - pos2[j]
            dis = min(dis, abs(diff))
            if diff < 0:
                i += 1
            else:
                j += 1
        return dis

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


'''
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = sys.maxint
        p1 = -1
        p2 = -1
        if word1 != word2:
            for i in range(len(words)):
                if words[i] == word1:
                    p1 = i
                if words[i] == word2:
                    p2 = i
                if p1 != -1 and p2 != -1:
                    dis = min(dis, abs(p1 - p2))
        else:
            for i in range(len(words)):
                if words[i] == word1:
                    if p1 == -1:
                        p1 = i
                    else:
                        if p2 == -1:
                            p2 = i
                        else:
                            p1 = p2
                            p2 = i
                        dis = min(dis, p2 - p1)
        return dis

# more briefy 
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        import sys
        p1 = -1
        p2 = -1
        dis = sys.maxint
        for k in range(len(words)):
            if words[k] == word1:
                p1 = k
            if words[k] == word2:
                if word1 == word2:
                    p1 = p2
                p2 = k
            if p1 != -1 and p2 != -1:
                dis = min(dis, abs(p2 - p1))
        return dis

