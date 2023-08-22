class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            min_height = min(height[i], height[j])
            cur_area = min_height * (j - i)
            max_area = max(cur_area, max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area