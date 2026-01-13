"""
2026.01.12
Plus One
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
"""
from typing import List

# O(n), O(n)
# 0ms. 19.43mb 6%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:       
        return list(map(int, str(int("".join(map(str, digits))) + 1)))

print(Solution().plusOne([9]))

