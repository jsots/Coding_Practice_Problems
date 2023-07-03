# Runtime 37.24% and Memory - 43.36%

# Important edge case - empty nums array. COrrected in the beginning. 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return None
        ans = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                end = nums[i-1]
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))
                start = nums[i]
        end = nums[-1]
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(end))
        return ans