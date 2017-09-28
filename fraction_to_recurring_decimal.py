'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''
# corner caser: 1, the numerator is 0; 2, the numerator can be divided by denominator; 3, one of them is negative;
# hash table: key is the remain; value is the starting point of a particular remain
# when find a same remain, divide the resulting string at the point that the remain firstly start, add "(" and ")" around the second substring  
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        ans = ""
        if (numerator < 0) ^ (denominator < 0):
            ans += "-"
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ans += str(numerator / denominator)
        
        remain = numerator % denominator
        if remain == 0:
            return ans
        
        ans += '.'
        remains = {}
        remains[remain] = len(ans)
        while remain:
            remain *= 10
            tmp = remain / denominator
            ans += str(tmp)
            remain %= denominator
            
            if remain in remains:
                pos = remains[remain]
                ans = ans[:pos] + "(" + ans[pos:] + ")"
                break
            
            remains[remain] = len(ans)  
        return ans
