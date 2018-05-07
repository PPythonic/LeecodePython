# coding=utf-8

"""
旋转数组--给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums


a = [1,2,3,4,5,6,7]
k = 3
b = Solution()
print (b.rotate(a, k))