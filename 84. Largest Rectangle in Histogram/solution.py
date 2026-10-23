class Solution:

    def find_next_smaller_elem(self, arr: list[int]) -> list[int]:
        stack = []
        n = len(arr)
        next_smaller_elem = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                next_smaller_elem[i] = stack[-1]

            stack.append(i)

        return next_smaller_elem

    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []
        n = len(heights)
        next_smaller_elem = self.find_next_smaller_elem(heights)
        max_Area = 0

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # find previous smaller element
            prev_smaller_elem = stack[-1] if stack else -1
            stack.append(i)

            max_Area = max(max_Area, heights[i] * (next_smaller_elem[i] - prev_smaller_elem - 1))

        return max_Area



