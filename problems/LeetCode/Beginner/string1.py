"""
2026.01.15
title: Reverse String
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/
"""
from typing import List

# first try
# 2ms 48%. 22%
# O(n) time, O(n) space
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[:] = reversed(s)
#         print(s)

# second try
# 0ms. 6%
# O(n) time, O(n) space
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[:] = s[::-1]
#         print(s)

# print(Solution().reverseString(["h","e","l","l","o"]))