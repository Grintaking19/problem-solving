class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # edge cases
        if not matrix:
            return matrix

        res = []
        row = len(matrix)
        col = len(matrix[0])
        while matrix and len(res) < row * col:
            # right direction
            if matrix[0]:
                res.extend(matrix.pop(0))
            # down direction
            if matrix and matrix[0]:
                for i in range(len(matrix)):
                    res.append(matrix[i].pop())
            # left direction
            if matrix:
                res.extend(matrix.pop()[::-1])
            # up direction
            if matrix and matrix[0]:
                for i in range(len(matrix) - 1, -1, -1):
                    res.append(matrix[i].pop(0))
        return res
