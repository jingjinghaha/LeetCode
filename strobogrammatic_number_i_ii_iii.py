'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        size = len(num) / 2
        for i in xrange(size+1):
            if num[i] not in mapping:
                return False
            if num[len(num)-1-i] != mapping[num[i]]:
                return False
        return True

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
'''
# divide & conquer
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)
    
    def helper(self, left, length):
        if left == 0:
            return ['']
        if left == 1:
            return ['0','1','8']
        
        prev = self.helper(left - 2, length)
        
        results = []
        for s in prev:
            if left != length:
                results.append('0'+s+'0')
            results.append('1'+s+'1')
            results.append('8'+s+'8')
            results.append('6'+s+'9')
            results.append('9'+s+'6')
        return results

# traverse
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        results = []
        self.helper(n, 0, n-1, ['0']*n, results)
        return results
    
    def helper(self, n, left, right, tmp, results):
        if left > right:
            results.append(''.join(tmp))
            return
        for key in self.mapping.keys():
            tmp[left] = key
            tmp[right] = self.mapping[key]
            if n != 1 and tmp[0] == '0':
                continue
            if left == right and key != self.mapping[key]:
                continue
            self.helper(n, left+1, right-1, tmp, results)

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''
# traverse
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        m = len(low)
        n = len(high)
        self.count = 0
        for i in range(m, n+1):
            self.helper(low, high, 0, i-1, ['0']*i)
        return self.count
    
    def helper(self, low, high, left, right, s):
        if left > right:
            if len(s) == len(low) and ''.join(s) < low:
                return
            if len(s) == len(high)  and ''.join(s) > high:
                return
            self.count += 1
            return
        for key in self.mapping.keys():
            s[left] = key
            s[right] = self.mapping[key]
            if len(s) != 1 and s[0] == '0':
                continue
            if left == right and key != self.mapping[key]:
                continue
            self.helper(low, high, left+1, right-1, s)

