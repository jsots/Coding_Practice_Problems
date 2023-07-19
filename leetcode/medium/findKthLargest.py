class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        ans = []
        while k > 0:
            ans.append(abs(heapq.heappop(nums)))
            k -= 1
        
        return ans[-1]