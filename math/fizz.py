# coding=utf-8

"""
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
"""


class Solution(object):
    def FizzBuzz(self, n):
        """
        :type n: int
        :rtype: list[str]
        """
        rlist = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                rlist.append("FizzBuzz")
            elif i % 3 == 0:
                rlist.append("Fizz")
            elif i % 5 == 0:
                rlist.append("Buzz")
            else:
                rlist.append(str(i))
        return rlist
