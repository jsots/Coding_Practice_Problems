class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,1
        total_water = 0

        while j < len(height):
            potential = 0
            if height[j] < height[i]:
                while height[j] < height[i] and j < len(height):
                    potential += height[i] - height[j]
                    j += 1
                if j > len(height):
                    potential = 0
                    i += 1
                    j = i +1
                else:
                    i = j
            total_water += potential
            i += 1
            j += 1
            print("i:", i, "j:", j, "total water---->", total_water)

        return total_water