# coding=utf-8

"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        import math
        power_list = str(math.log(n, 3)).split(".")
        if power_list[1] == "0":
            return True
        return False


class Solution2(object):
    # 速度更快,没使用内部模块
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype bool
        """
        while n % 3 == 0 and n > 1:
            n = n/3
        return n == 1
