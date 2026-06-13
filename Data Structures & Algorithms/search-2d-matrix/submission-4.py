class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r: 
            mid = l + ((r - l) // 2)
            print(f"mid: {mid}")
            if matrix[mid][0] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                return True    

        ind = r
        if ind < 0:
            return False
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            #print(f"mid: {mid}")
            if matrix[ind][mid] < target:
                l = mid + 1
            elif matrix[ind][mid] > target:
                r = mid - 1
            else:
                return True 
        return False       