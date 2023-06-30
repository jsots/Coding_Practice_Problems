class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target not in nums:
                if nums[i] == target-1:
                    return i+1
                if nums[i] == target+1:
                    return i
            if nums[i] == target:
                return i
        return None