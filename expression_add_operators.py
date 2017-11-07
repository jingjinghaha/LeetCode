'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''
# DFS, backtracking
# time: O(3^n * n * (n-1) * (n-2) * ... * 1)
# space: O(n) * time
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        if not num:
            return []
        num = str(num)
        self.helper(num, target, 0, 0, [], '', results)
        return results
    def helper(self, num, target, res, start, stack, tmp, results):
        if start == len(num):
            if target == res:
                results.append(tmp)
            return
        for i in range(start, len(num)):
            if i != start and num[start] == '0':
                break
            cur = num[start: i+1]
            if start == 0:
                self.helper(num, target, int(cur), i + 1, [int(cur)], cur, results)
            else:
                self.helper(num, target, res + int(cur), i + 1, stack + [int(cur)], tmp + '+' + cur, results)
                self.helper(num, target, res - int(cur), i + 1, stack + [-int(cur)], tmp + '-' + cur, results)
                prev = stack[-1]
                product = prev * int(cur)
                self.helper(num, target, res - prev + product , i + 1, stack + [product], tmp + '*' + cur, results)

# a little bit optimization on space (as the product rely only on the last element of the stack in previous solution, use a single variable - product - to store the last value of previous stack)
# time: O(3^n * n * (n-1) * (n-2) * ... * 1)
# space: O(1) * time
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        if not num:
            return []
        num = str(num)
        self.helper(num, target, 0, 0, 0, '', results)
        return results
    def helper(self, num, target, res, start, product, tmp, results):
        if start == len(num):
            if target == res:
                results.append(tmp)
            return
        for i in range(start, len(num)):
            if i != start and num[start] == '0':
                break
            cur = num[start: i+1]
            if start == 0:
                self.helper(num, target, int(cur), i + 1, int(cur), cur, results)
            else:
                self.helper(num, target, res + int(cur), i + 1, int(cur), tmp + '+' + cur, results)
                self.helper(num, target, res - int(cur), i + 1, -int(cur), tmp + '-' + cur, results)
                self.helper(num, target, res - product + product * int(cur) , i + 1, product * int(cur), tmp + '*' + cur, results)


