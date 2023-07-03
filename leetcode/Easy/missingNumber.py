class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = 0
        for missing_number in range(len(nums)):
            if missing_number not in nums:
                return missing_number
            else:
                missing_number += 1
        return missing_number