class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # bit mask solution (very fast and memory efficient)
        # fast -> bit operations are done by native cpu assembly instructions in one clock cycle
        # memory efficient: because hashs and sets require dynamic memory allocations

        rows = [0] * 9
        columns = [0] * 9
        squares = [0] * 9


        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                digit = int(board[r][c]) # 0-indexed bitmasking
                digit_mask = 1 << digit
                square_idx = (r // 3) * 3 + (c // 3)
                if (digit_mask & rows[r]) or (digit_mask & columns[c]) or (digit_mask & squares[square_idx]):
                    return False
                rows[r] |= digit_mask
                columns[c] |= digit_mask
                squares[square_idx] |= digit_mask

        return True