# coding=utf8

"""
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
7.     13112221
8.     1113213211
9.     31131211131221
10.    13211311123112112211
给定一个正整数 n ，输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。
"""

# 思路：循环先前生成的序列，当发现两个不同的数时，添加[1,num]到新的序列中，发现相同的
# 数时，添加[count, num]到新的序列中


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = [1]
        for _ in range(n-1):
            next = []
            for num in sequence:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
            sequence = next

        return "".join(map(str, sequence))


n = 10
a = Solution()
print(a.countAndSay(n))