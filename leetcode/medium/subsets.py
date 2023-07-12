class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []

        def dfs(i):
            # Base case - out of bounds
            if i >= len(nums):
                ans.append(sub.copy())
                return
            
            # Decide to add the number

            sub.append(nums[i])
            dfs(i+1)

            # decide to not add number
            sub.pop()
            dfs(i+1)
            
        dfs(0)
        return ans