# Runtime - 32.48% and Memory - 61.66%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans