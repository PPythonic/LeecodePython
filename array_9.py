# coding=utf-8

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例：给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

# 方法1，4000+ms测试通过时间
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = len(nums)
        for i in range(a-1):
            for j in range(i+1,a):
                if nums[i] + nums[j] == target:
                    return [i,j]


# 方法2，32ms测试通过时间
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)  
        #创建一个空字典  
        d = {}  
        for x in range(n):  
            a = target - nums[x]  
            #字典d中存在nums[x]时  
            if nums[x] in d:  
                return d[nums[x]],x  
            #否则往字典增加键/值对  
            else:  
                d[a] = x  

nums = [2,7,11,15]
target = 9
a = Solution()
print(a.twoSum(nums, target))
