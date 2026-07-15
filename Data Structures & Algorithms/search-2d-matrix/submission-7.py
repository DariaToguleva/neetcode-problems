class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1
        row = -1

        while u <= d:
            mid = u + ((d - u) // 2)

            if matrix[mid][0] < target:
                row = mid
                u = mid + 1
            elif  matrix[mid][0] > target:  
                d = mid - 1
            else:
                return True    
        print(row)

        l = 0
        r = len(matrix[mid]) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[row][m] < target:
                l = m + 1
            elif  matrix[row][m] > target:  
                r = m - 1
            else:
                return True

        return False     