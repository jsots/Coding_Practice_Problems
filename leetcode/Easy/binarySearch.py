class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        if left == right:
            if nums[left] == target:
                return left
        while left < right:
            print(left)
            print(right)
            mid = math.floor((right + left)/2)
            if nums[mid] < target:
                left = mid+1
            if nums[mid] > target:
                right = mid
            if nums[mid] == target:
                return mid
            if nums[right] == target:
                return right
        return -1