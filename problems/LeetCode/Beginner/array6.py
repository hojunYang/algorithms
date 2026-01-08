"""
2026.01.08
title: Intersection of Two Arrays II
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/
"""
from typing import List
# first try 0ms. 19.36mb 5%.
# O(n + m) time, O(n + m) space
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        list = []
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1
        for num in dict1:
            if num in dict2:
                list.extend([num] * min(dict1[num], dict2[num]))
        return list

print(Solution().intersect([1,2,2,1], [2,2]))