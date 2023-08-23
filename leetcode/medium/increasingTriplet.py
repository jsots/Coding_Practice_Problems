class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 2):
            first = nums[i]
            for j in range(i + 1, len(nums) - 1):
                if nums[j] > first:
                    second = nums[j]
                    for k in range(j + 1, len(nums)):
                        if nums[k] > second:
                            return True

        return False