# coding=utf8

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(-price, buy)
            sell = max(price + buy, sell)

        return sell


a = Solution()
print a.maxProfit([7,1,5,3,6,4])