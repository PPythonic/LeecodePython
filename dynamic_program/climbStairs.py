# coding=utf8

"""
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            temp = 0
            for i in range(3, n+1):
                temp = a + b
                a, b = b, temp
            return temp


a = Solution()
print a.climbStairs(10)
