"""
2026.01.13
Valid Sudoku
link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/
"""
from typing import ForwardRef, List

# first try
# 7ms. 5%
# O(1), O(1)
# from itertools import product
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i, j in product(range(3), range(3)):
#             block = list(board[i*3+0][j*3:j*3+3]) + list(board[i*3+1][j*3:j*3+3]) + list(board[i*3+2][j*3:j*3+3])
#             block = [_ for _ in block if _ != '.']
#             if len(block) != len(set(block)):
#                 return False
#         for i in range(9):
#             row = list(board[i])
#             row = [_ for _ in row if _ != '.']
#             if len(row) != len(set(row)):
#                 return False
#         for j in range(9):
#             col = [board[i][j] for i in range(9)]
#             col = [_ for _ in col if _ != '.']
#             if len(col) != len(set(col)):
#                 return False
#         return True

# second try
# 0ms. 5%
# O(1), O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, j in (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2):
            block = list(board[i*3+0][j*3:j*3+3]) + list(board[i*3+1][j*3:j*3+3]) + list(board[i*3+2][j*3:j*3+3])
            block = [_ for _ in block if _ != '.']
            if len(block) != len(set(block)):
                return False
        for i in range(9):
            row = [_ for _ in board[i] if _ != '.']
            if len(row) != len(set(row)):
                return False
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            col = [_ for _ in col if _ != '.']
            if len(col) != len(set(col)):
                return False
        return True

print(Solution().isValidSudoku([
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))