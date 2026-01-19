"""
2026.01.19
title: Climbing Stairs
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/569/
"""

# first try
# 0ms. 20%
# O(n), O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        while len(dp) < n :
            dp.append(dp[-1] + dp[-2])
        return dp[n - 1]


print(Solution().climbStairs(5))