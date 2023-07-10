class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_ind = stack.pop()
                ans[stack_ind] = (i - stack_ind)
            stack.append([t,i])
        
        return ans