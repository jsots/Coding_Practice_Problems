class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        cur_avg = cur_sum/k
        max_avg = cur_avg

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            cur_avg = cur_sum/k
            max_avg = max(cur_avg, max_avg)

        return max_avg

