# coding=utf-8

"""
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_lst = set(nums)
        if len(nums) == len(new_lst):
            return False
        return True


# lst = [1,2,3,4]
lst = []
a = Solution()
print (a.containsDuplicate(lst))