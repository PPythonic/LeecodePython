# coding=utf-8

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0 for _ in range(26)]

        for c in s:
            counts[ord(c) - ord("a")] += 1

        for i, c in enumerate(s):
            if counts[ord(c) - ord("a")] == 1:
                return i

        return -1

        
s = "bcbbca"
a = Solution()
print a.firstUniqChar(s)