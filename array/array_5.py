# coding=utf-8

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
# 任何数和它自己按位异或都是0


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype nums: int
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor


lst = [1,2,3,4,5,3,4,1,2]
a = Solution()
print (a.singleNumber(lst))