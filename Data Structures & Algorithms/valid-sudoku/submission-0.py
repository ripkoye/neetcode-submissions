class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for r in range(0, 9):
            row = set()
            col = set()
            for c in range(0, 9):
                #getting row, just need to check duplicate
                if board[r][c] != '.':
                    if board[r][c] in row:
                        return False
                    else:
                        row.add(board[r][c])
                if board[c][r] != '.':
                    if board[c][r] in col:
                        return False
                    else:
                        col.add(board[c][r])
        # now we need to solve center board.
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = set()

                for i in range(3):
                    for j in range(3):
                        val = board[r+i][c+j]

                        if val == ".":
                            continue

                        if val in box:
                            return False

                        box.add(val)
        return True
