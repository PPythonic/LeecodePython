# coding=utf-8

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxsum = float('-inf')
        # length = len(nums)

        # for i in range(length):
        #     for j in range(i, length):
        #         maxsum = max(maxsum, sum(nums[i:j+1]))

        # return maxsum

        overall_max = float('-inf')
        max_ending_here = 0

        for num in nums:
            if max_ending_here > 0:
                max_ending_here += num
            else:
                max_ending_here = num
            overall_max = max(overall_max, max_ending_here)
        
        return overall_max


a = Solution()
b = [-2,1,-3,4,-1,2,1,-5,4]
# b = [-2, -1]
print a.maxSubArray(b)