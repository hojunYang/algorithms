"""
2026.01.08
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/
"""
import time
from typing import List
# first try 0ms 100%. 21.68mb 5%.
# O(n) time, O(n) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        return num_set.pop()
print(Solution().singleNumber([4,1,2,1,2]))