from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            row = set()
            for num in l:
                if num == '.':
                    continue
                elif num in row:
                    return False
                else:
                    row.add(num)
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] == '.':
                   continue
                elif board[j][i] in col:
                    return False
                else:
                    col.add(board[j][i])
        dictionary = {}
        
        for i in range(9):
            for j in range(9):
                key = (i // 3, j // 3)
                if key not in dictionary:
                    dictionary[key] = set()
                val = board[j][i]
                if val == '.':
                    continue
                elif val in dictionary[key]:
                    return False
                else:
                    dictionary[key].add(val)
        return True
        