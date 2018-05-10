# coding=utf-8

"""
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


# class Solutions(object):
#     def plusone(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         i = len(digits)-1
#         while i >= 0 and digits[i] == 9:
#             digits[i] = 0
#             i -= 1

#         if i == -1:
#             return [1] + digits
#         return digits[:i] + [digits[i]+1] + digits[i+1:]


# 方法二
class Solutions(object):
    def plusone(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # str和int转换
        sum = 0
        for i in digits:
            sum = sum*10 + i
        return [int(x) for x in str(sum+1)]



# lst = [9]
lst = [1,2,3,4]
a = Solutions()
print a.plusone(lst)