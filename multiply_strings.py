'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return None
        product = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1 , -1):
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j])
                tmp += product[i + j + 1]
                product[i + j] += tmp / 10
                product[i + j + 1] = tmp % 10
        s = ''
        for i in range(len(product)):
            if s == '' and product[i] == 0:
                continue
            s += str(product[i])
        if s == '':
            return '0'
        return s

