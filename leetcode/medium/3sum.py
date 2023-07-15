class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() # Begin by sorting
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans

# Attempting again. I know im close!

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # sort to start, that way it will be two sum 2 moving forward
        for i, a in enumerate(nums):
            j = i+1
            k = len(nums) - 1
            while j < k:
                need = -a
                if nums[j] + nums[k] < need:
                    j += 1
                elif nums[j] + nums[k] > need:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    break
        return ans