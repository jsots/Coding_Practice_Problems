class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        subset = []

        def dfs(i):
            # Base case:
            if i >= len(nums):
                if subset not in ans:
                    ans.append(subset.copy())
                return
            
            # decide if adding the number:

            subset.append(nums[i])
            dfs(i+1)

            # decide to not add anything
            subset.pop()
            dfs(i+1)

        dfs(0)
        return ans