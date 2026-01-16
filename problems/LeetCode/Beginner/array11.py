"""
2026.01.15
title: Rotate Image
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/"""

from typing import List
# first try
# 0ms. 13.6%
# O(n^2) time, O(n^2) space
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         matrix[:] = [[matrix[j][i] for j in range(len(matrix)-1, -1, -1)] for i in range(len(matrix))]
#         print(matrix)

# second try made by LLM
# 0ms. 5%
# O(n^2) time, O(n^2) space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] =  list(zip(*matrix[::-1]))
        print(matrix)
print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))