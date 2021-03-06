# coding=utf-8
from collections import Counter


"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
输入: s = "anagram", t = "nagaram"
输出: true
"""


# 方法一，可以实现，但是执行时间过长
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = {c: s.count(c) for c in s}
        t = {c: t.count(c) for c in t}
        for c, n in s.items():
            if c in t:
                if t[c] == n:
                    continue
                else:
                    return False
            else:
                return False
        return True


# 方法二
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
a = Solution()
print a.isAnagram(s, t)