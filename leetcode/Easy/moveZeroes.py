class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        z = 1

        while z < len(nums):
            if nums[n] == 0:
                if nums[z] != 0:
                    temp = nums[z]
                    nums[z] = nums[n]
                    nums[n] = temp
                    n += 1
                z += 1
            else:
                n += 1
                z += 1
        return nums