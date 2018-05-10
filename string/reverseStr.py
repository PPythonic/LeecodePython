# coding=utf-8

"""
请编写一个函数，其功能是将输入的字符串反转过来。
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]  # 字符串可切片，可迭代
        
        
s = 'Hello'
a = Solution()
print a.reverseString(s)