"""
2026.01.07
링크: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

"""

from typing import List

# first try
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         index = 0;
#         for i in range(len(nums)):
#             if nums[i] != nums[index]:
#                 index += 1
#                 nums[index] = nums[i]
#         return nums

# second try
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set[int](nums))
        return len(nums)


print(Solution().removeDuplicates([1, 1, 2]))
