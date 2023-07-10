class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for row in range(len(board)):
            print(check)
            for i in range(9):
                if board[row][i] not in check and board[row][i] != ".":
                    check.add(board[row][i])
                    print(board[row][i])
                elif board[row][i] == ".":
                    pass
                else: 
                    print(board[row][i])
                    return False
            check.clear()
        for col in range(9):
            for i in range(9):
                if board[col][i] not in check and board[col][i] != ".":
                    check.add(board[col][i])
                    print(board[col][i])
                elif board[col][i] == ".":
                    pass
                else:
                    return False
            check.clear()
        for box_row in range(3):
            for box_col in range(3):
                if board[box_row][box_col] not in check and board[box_row][box_col] != ".":
                    check.add(board[box_row][box_col])
                    print(board[box_row][box_col])
                elif board[box_row][box_col] == ".":
                    pass
                else: 
                    return False
        return True 