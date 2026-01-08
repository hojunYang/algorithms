"""
2026.01.08
LINK: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
"""
import time
from typing import List
# first try 9ms 92%. 31.26mb 66%. second 2ms 98.78%. 아 이거 몰랐는데 그냥 시도할때마다 좀 달라짐..
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))

# second try 15ms 50%. 32.55mb 20%.
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums_set = set()
#         for num in nums:
#             if num in nums_set:
#                 return True
#             nums_set.add(num)
#         return False
