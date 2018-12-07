# coding=utf-8

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution(object):
    """
    这版只能接受s为小写字母的集合
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        glist = [0 for x in range(26)]
        rlist = []
        mint = 0
        if len(s) < 2:
            return len(s)
        for x in range(len(s)):
            for i in range(x, len(s)):
                glist[ord(s[i]) - ord('a')] += 1
                mint += 1
                if max(glist) > 1:
                    glist = [0 for x in range(26)]
                    rlist.append(mint-1)
                    mint = 0
                    break
        return max(rlist)


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        l = 0
        for i in range(len(s)):
            cur = s[i]
            if cur not in d.keys():
                d[cur] = i
            else:
                if d[cur] + 1 > start:
                    start = d[cur] + 1
                d[cur] = i
            if i - start + 1 > l:
                l = i - start + 1
        return l


test = Solution2()
s = "abc123%$"
print test.lengthOfLongestSubstring(s)
