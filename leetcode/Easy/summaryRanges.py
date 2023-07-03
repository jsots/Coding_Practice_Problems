class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1 
            else:
                frequency[num] = 0
        return max(frequency, key=frequency.get)