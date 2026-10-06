# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# [0 0]
# row =       0          123456789
# col =       123456789  0
# quadrant =  0-2 0-2

# [3 4]
# row =       3          123456789 i
# col =       123456789  4         j
# quadrant =  3-5 3-5.             

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        rows = defaultdict(set)
        cols = defaultdict(set)
        quadrants = defaultdict(set)
        for j in range(9):
            for i in range(9):

                e = board[i][j]
                if e == '.':
                    continue
                
                e = int(e)
                q = (i // 3, j // 3)

                if (e in rows[i]) or (e in cols[j]) or (e in quadrants[q]):
                    return False
                else:
                    rows[i].add(e)
                    cols[j].add(e)
                    quadrants[(i // 3, j // 3)].add(e)

        return True
        
        