class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        # first binary search for the row the target is in

        top = 0
        bot = rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        # second binary search to find the target value
        row = (top + bot) // 2
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False


