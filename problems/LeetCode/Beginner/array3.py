"""
2026.01.07
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/
"""

from typing import List

# first try 1781ms. 26.48mb
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#             nums.insert(0, nums.pop())
#         print(nums)

# second try failed
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nums[:] = nums[-k:] + nums[:-k]
#         print(nums)

# third try Time Limit Exceeded
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#             nums[:] = nums[-1:] + nums[:-1]
#         print(nums)


# fourth try 3ms 75.16%. 26.45mb. 6.11%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


print(Solution().rotate([1, 2], 7))
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
