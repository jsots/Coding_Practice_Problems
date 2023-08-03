# O(n) time and O(n) space

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        for num in candies:
            max_candies = max(max_candies, num)
        
        ans = []
        for num in candies:
            if num + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans