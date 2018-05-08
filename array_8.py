# coding=utf-8

"""
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。
例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。
必须在原数组上操作，不要为一个新数组分配额外空间。
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = len(nums)
        b = nums.count(0)
        nums[:a-b] = filter(None, nums)
        nums[a-b:] = [0] * b
        return nums
        

nums = [0,1,0,3,12]
a = Solution()
print(a.moveZeroes(nums))
