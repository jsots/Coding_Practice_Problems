class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        ans = []
        for num in nums:
            if num not in ans:
                seen[num] = 1
            else:
                seen[num] += 1
        for i in range(k):
            a = max(seen, key=seen.get)
            ans.append(a)
            seen.pop(a)
        return ans
