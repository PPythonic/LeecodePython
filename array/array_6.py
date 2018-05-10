# coding=utf-8

from collections import Counter

"""
给定两个数组，写一个方法来计算它们的交集。
例如：给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
"""


class Solutions(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq1 = Counter(nums1)

        result = []
        for i, num in enumerate(nums2):
            if num in freq1 and freq1[num] > 0:
                freq1[num] -= 1
                result.append(num)
        return result
