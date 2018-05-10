# coding=utf-8

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         i = 0
#         while i < len(nums)-1:
#             if nums[i] == nums[i+1]:
#                 nums.remove(nums[i])
#             else:
#                 i += 1
#         return len(nums)


# 比上个方法快10多倍，思想：直接把互不相等的数字放到数组的前面，之后删除重复的数字
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        for x in range(1, len(nums)):
            if nums[x] != nums[i]:
                i += 1
                nums[i] = nums[x]

        del nums[i:len(nums)-1]

        return len(nums)


lst = [1,1,2,2,3,3,4,4,5]
a = Solution()
print a.removeDuplicates(lst)