# coding=utf-8

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        reversed = 0
        while x != 0:
            reversed = reversed * 10 + x % 10  # 整数的翻转除10取余,之后每次循环乘10来实现翻转。妙啊
            x //= 10

        if reversed > 2**31 - 1:
            return 0
        return reversed if not negative else -reversed


number = -123
a = Solution()
print a.reverse(number)
