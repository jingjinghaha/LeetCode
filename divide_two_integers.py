'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''
ass Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == - 2**31 and divisor == -1):
            return 2**31 - 1
        neg = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        times = 0
        while dividend >= divisor:
            tmp = divisor
            cnt = 1
            while dividend >= tmp << 1:
                tmp = tmp << 1
                cnt = cnt << 1
            dividend -= tmp
            times += cnt
        if neg:
            return - times
        return times
