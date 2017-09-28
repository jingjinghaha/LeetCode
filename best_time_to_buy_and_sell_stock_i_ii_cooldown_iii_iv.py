'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) < 2:
            return profit
        min = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min)
            if prices[i] < min:
                min = prices[i]
        return profit

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
# the trick is to add every increase 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit +=  prices[i] - prices[i-1]
        return profit

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
# dynamic programming: 
# sell[i] means before day i what is the maxProfit for any sequence end with sell
# buy[i] means before day i what is the maxProfit for any sequence end with buy
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        sell[0] = 0
        buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            if i > 1:
                buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            else:
                buy[i] = max(buy[i-1], - prices[i])
        
        return sell[-1]

# futher reduce space as states of day i relies only on i-1 and i-2
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        sell = 0
        buy = -prices[0]
        prev_sell = 0
        prev_buy = 0
        
        for i in range(1, len(prices)):
            prev_buy = buy
            buy = max(buy, prev_sell - prices[i])
            prev_sell = sell
            sell = max(sell, prev_buy + prices[i])
            
        return sell


'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

