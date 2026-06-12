class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterarte over rows 
        for row in range(9):
            row_dict = {}
            for i in range(9):
                if board[row][i] in row_dict and board[row][i] != '.':
                    return False
                else: row_dict[board[row][i]] = 1
        
        # Iterate over columns
        for j in range(9):
            column_dict = {}
            for column in range(9):
                if board[column][j] in column_dict and board[column][j] != '.':
                    return False
                else: column_dict[board[column][j]] = 1
        
        # empty old dict
        row_dict = {}
        column_dict = {}
        
        # Iterate over boxes
        for square in range(9):
            box_dict = {}
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    column = (square % 3) * 3 + j
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in box_dict:
                        return False
                    box_dict[board[row][column]] = 1

        return True