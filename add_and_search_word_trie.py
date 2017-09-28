'''
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or '.'. A '.' means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
'''

class Node():
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)

    def dfs(self, word, node):
        if not word:
            return node.word
            
        if not node:
            return False
        
        if word[0] == '.':
            for key in node.children.keys():
                if  not node.children[key]:
                    return False
                if self.dfs(word[1:], node.children[key]):
                    return True
        else:
            if word[0] not in node.children:
                return False
            if not node.children[word[0]]:
                return False
            return self.dfs(word[1:], node.children[word[0]])
            
        return False
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
