# coding=utf8

"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""


# 方法一
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        lh = len(haystack)
        if ln == 0:
            return 0
        if haystack == needle:
            return 0
        for i in range(lh-ln+1):
            # print(haystack[i:i+ln])
            if haystack[i:i+ln] == needle:
                return i
        return -1


# 方法二
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not len(needle):
            return 0
        return haystack.find(needle)  # python中内置的find方法


haystack = "mississippi"
needle = 'pi'
a = Solution2()
print(a.strStr(haystack, needle))
