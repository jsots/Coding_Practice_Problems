class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        total_product = 1
        zero = False
        for num in nums:
            if num != 0:
                total_product *= num
            if num == 0:
                zero = True
        for num in nums:
            if num != 0 and zero:
                ans.append(0)
            if num != 0 and not zero:
                ans.append(total_product//num)
            if num == 0 and zero:
                ans.append(total_product)
        return ans