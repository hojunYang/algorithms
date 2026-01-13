"""
2026.01.13
Two Sum
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/
"""
from typing import List
# from itertools import combinations
# first try
# O(n^2), O(n)
# 1995ms 8%, 19.86mb 9.72%
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for (i, j) in (combinations(range(len(nums)), 2)):
#             if nums[i] + nums[j] == target and i != j:
#                 return [i, j]

# second try failed
# O(n^2), O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numss = [(i, j) for i, j in enumerate(nums) if j <= target]
#         for (i, j) in numss:
#             for (k, l) in numss:
#                 if i != k and j + l == target:
#                     return [i, k]
        
# third try
# 4ms. 5%
# O(n), O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target - num]:
                return [i, nums_dict[target - num]]
print(Solution().twoSum([2,8,11,7], 9))
print(Solution().twoSum([3,3], 6))
print(Solution().twoSum([-3,4,3,0], 0))
print(Solution().twoSum([0,4,3,0], 0))
