class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            width = (j - i)
            if height[i] < height[j]:
                current_area = height[i] * width
                i += 1
            else:
                current_area = height[j] * width
                j -= 1
            if max_area < current_area:
                max_area = current_area
            print(height[i], height[j], max_area)
        return max_area