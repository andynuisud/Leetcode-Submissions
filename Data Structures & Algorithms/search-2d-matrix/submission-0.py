class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        subArrayVal = -1
        
        for i in range(len(matrix)):

            if matrix[i][0] <= target <= matrix[i][-1]:
                subArrayVal = i
                break

        if subArrayVal == -1: 
            return False

        left = 0
        right = len(matrix[subArrayVal]) - 1

        while left <= right: 
            
            middle = left + (right - left) // 2

            if target == matrix[subArrayVal][middle]:
                return True
            elif target < matrix[subArrayVal][middle]:
                right = middle - 1
            else:
                left = middle + 1

        return False