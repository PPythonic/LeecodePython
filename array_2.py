# coding=utf-8

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days == 0:
            return 0
        if prices == sorted(prices)[::-1]:
            return 0
        if prices == sorted(prices):
            return prices[-1]-prices[0]
        else:
            profit = 0
            for p in range(1, days):
                if prices[p] > prices[p-1]:
                    profit += (prices[p]-prices[p-1])

            return profit


lst = [7,1,5,3,6,4]
# lst = [1,2,3,4,5]
a = Solution()
print a.maxProfit(lst)
