# coding=utf-8

'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
输入: num1 = "2", num2 = "3"
输出: "6"
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """ 
        if len(num1) > 110 or len(num2) > 110:
            return 
        int_num1 = int(num1)
        int_num2 = int(num2)
        return str(int_num1 * int_num2)
