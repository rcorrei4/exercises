from collections import defaultdict
from typing import List

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in board:
#             hashset = set()
#             for number in row:
#                 if number in hashset and number != '.':
#                     return False
#                 hashset.add(number)
                
#         for columm in range(9):
#             hashset = set()
#             for number in range(9):
#                 if board[number][columm] in hashset and board[number][columm] != '.':
#                     return False
#                 hashset.add(board[number][columm])
                
#         hashmap = defaultdict(set)
#         for row in range(9):
#             for columm in range(9):
#                 hashmap_row = (row//3)
#                 hashmap_columm= (columm//3)
                
#                 if board[row][columm] != '.':
#                     if board[row][columm] in hashmap[tuple([hashmap_row, hashmap_columm])]:
#                         return False
#                     hashmap[tuple([hashmap_row, hashmap_columm])].add(board[row][columm])
#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columms = defaultdict(set)
        squares = defaultdict(set)
        
        for row in range(9):
            for columm in range(9):
                if board[row][columm] != '.':
                    if (board[row][columm] in rows[row] or
                        board[row][columm] in columms[columm] or
                        board[row][columm] in squares[(row//3, columm//3)]):
                        return False
                    rows[row].add(board[row][columm])
                    columms[columm].add(board[row][columm])
                    squares[(row//3, columm//3)].add(board[row][columm])
        return True