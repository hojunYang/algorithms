"""
2026.01.13
Move Zeroes
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/
"""
from typing import List

# O(n), O(1)
# 7ms. 20.46mb 11%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = sorted(nums, key=lambda x: x == 0)

print(Solution().moveZeroes([0,1,0,3,12, 3]))