# coding=utf-8

'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
attention:输入的字符串只包含小写字母; 两个字符串的长度都在 [1, 10,000] 之间
'''

class Solution(object):
    """
    会超出时间限制
    """
    def checkInClusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len = len(s1)
        s2_len = len(s2)
        from collections import Counter
        s1_counter = Counter(s1)
        for i in range(s2_len - s1_len+1):
            s2_counter = Counter(s2[i:i+s1_len])
            if s1_counter == s2_counter:
                return True
        return False


class Solution2(object):
    """
    滑动窗口法,TO(l1 + 26*(l2-l1))
    """
    def checkInClusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        for i in range(len_s1):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1
        for i in range(len_s2 - len_s1):
            if self.match(list1, list2):
                return True
            list2[ord(s2[i + len(s1)]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] -= 1
        return self.match(list1, list2)

    def match(self, list1, list2):
        for i in range(26):
            if list1[i] != list2[i]:
                return False
        return True


test = Solution2()
s1 = 'abc'
s2 = 'bbbca'
print test.checkInClusion(s1, s2)
            
