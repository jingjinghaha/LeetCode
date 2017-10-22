'''
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
'''
class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        from collections import deque
        self.letter_list = deque()
        i = 0
        while i < len(compressedString):
            if compressedString[i].isalpha():
                self.letter_list.append(compressedString[i])
                i += 1
            else:
                j = i
                while j < len(compressedString) and not compressedString[j].isalpha():
                    j += 1
                self.letter_list.append(int(compressedString[i:j]))
                i = j

    def next(self):
        """
        :rtype: str
        """
        if len(self.letter_list) > 1:
            res = self.letter_list[0]
            self.letter_list[1] -= 1
            if self.letter_list[1] == 0:
                self.letter_list.popleft()
                self.letter_list.popleft()
            return res
        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.letter_list) > 1

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

