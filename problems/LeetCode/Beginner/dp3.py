"""
2026.01.21
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/566/
"""
from typing import List

# first try
# O(n), O(n)
# 65ms 44%. 41%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))
