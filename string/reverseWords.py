# coding=utf-8

"""
给定一个字符串，逐个翻转字符串中的每个单词。
示例:  ----输入: "the sky is blue",
输出: "blue is sky the".
说明:无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: string
        :rtype string
        """
        w_list = s.split(" ")[::-1]
        new_s = ""
        for i in range(len(w_list)):
            if w_list[i] != "":
                new_s += " "
                new_s += w_list[i]
        return new_s.lstrip()
