class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        piv_idx = -1
        left_sum = 0
        right_sum = sum(nums[1:])

        for i in range(1, len(nums)):
            print("L: ", left_sum, "R: ", right_sum)
            if left_sum == right_sum:
                piv_idx = i-1
                return piv_idx
            left_sum += nums[i-1]
            right_sum -= nums[i]
        
        if left_sum == right_sum:
            piv_idx = i

        return piv_idx