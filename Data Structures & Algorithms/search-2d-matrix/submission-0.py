class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_outer = left_inner = 0
        right_outer = len(matrix) - 1
        right_inner = len(matrix[0]) - 1

        while left_outer <= right_outer:
            midpoint_outer = left_outer + (right_outer - left_outer) // 2
            if matrix[midpoint_outer][0] <= target <= matrix[midpoint_outer][-1]:
                while left_inner <= right_inner:
                    midpoint_inner = left_inner + (right_inner - left_inner) // 2
                    if matrix[midpoint_outer][midpoint_inner] == target:
                        return True
                    elif matrix [midpoint_outer][midpoint_inner] < target:
                        left_inner = midpoint_inner + 1
                    else:
                        right_inner = midpoint_inner - 1
                return False
            
            elif matrix[midpoint_outer][-1] < target:
                left_outer = midpoint_outer + 1
            else:
                right_outer = midpoint_outer - 1
        return False



