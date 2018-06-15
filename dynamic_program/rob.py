# coding=utf-8

"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""

"""
一般来说,给定一个规则,求解任意状态下的解,就是用动态规划.这里的规则是劫匪不能同时抢劫相邻的房子,即我们做累加时,
只有两种选择:
1.如果选择抢劫了上一个屋子,就不能抢劫当前屋子,所以最大收益是抢劫上一个屋子的收益;
2.如果选择抢劫了当前屋子,就不能抢劫之前的屋子,所以最大收益是上一个屋子的上一个屋子抢劫的钱,加上当前屋子抢劫的钱
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        loot, prev = nums[0], 0

        for num in nums[1:]:
            loot, prev = max(num+prev, loot), loot
        
        return loot


lst = [2,7,9,3,1]
a = Solution()
print a.rob(lst)