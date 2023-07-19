class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_m = 0
        right_m = len(matrix)
        while left_m < right_m:
            mid = (left_m + right_m)//2
            print(mid)
            if matrix[mid][0] > target:
                right_m = mid - 1
            elif matrix[mid][0] < target:
                left_m = mid + 1
            if matrix[mid][0] == target:
                left_m = right_m = mid
                break
        
        left_n = 0
        right_n = len(matrix[0])

        if left_m >= len(matrix) or target < matrix[left_m][0]:
            return False


        while left_n < right_n:
            mid = (left_n + right_n)//2
            print("mid:", mid, "row:", left_m)
            if matrix[left_m][mid] > target:
                right_n = mid - 1
            elif matrix[left_m][mid] < target:
                left_n = mid + 1
            if matrix[left_m][mid] == target:
                left_n = right_n = mid
                break
        
        if matrix[left_m][left_n] == target:
            return True
        return False



# Solved on a new day:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) - 1, len(matrix[0]) -1
        top, bot = 0, rows

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        row = (top + bot) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False

    