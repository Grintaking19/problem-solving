class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        # get the row
        while bottom <= top and l <= r :
            mid = bottom + (top - bottom) // 2
            mid_matrix = matrix[mid]
            if mid_matrix[r] >= target and mid_matrix[l] <= target:
                if mid_matrix[r] == target or mid_matrix[l] == target:
                    return True
                while l <= r: 
                    mid_column = l + (r - l) // 2
                    if target == mid_matrix[mid_column]:
                        return True 
                    elif target > mid_matrix[mid_column]:
                        l = mid_column + 1
                    else:
                        r = mid_column - 1
                return False
            elif mid_matrix[l] > target:
                top = mid - 1
            elif mid_matrix[r] < target:
                bottom = mid + 1
        return False