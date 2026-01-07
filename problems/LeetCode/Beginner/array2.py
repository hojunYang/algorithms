"""
2026.01.07
링크: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
"""

from typing import List

# first try 2ms
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 max_profit += prices[i] - prices[i-1]
#         return max_profit

# second try 3ms
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))


# third try 0ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(
            prices[i + 1] - prices[i]
            for i in range(len(prices) - 1)
            if prices[i + 1] > prices[i]
        )


print(Solution().maxProfit([1, 2, 3, 4, 5]))
