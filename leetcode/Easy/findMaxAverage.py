def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])  # Calculate initial sum of the first k elements
        max_avg = current_sum / k  # Initialize max_avg with the average of the first k elements

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Update the current sum by subtracting the leftmost element and adding the rightmost element
            max_avg = max(max_avg, current_sum / k)  # Update the max_avg if a higher average is found

        return max_avg