class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        for i in range(len(numbers)):
            while numbers[i] + numbers[j] < target:
                i += 1
            while numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target and i != j:
                return [i+1, j+1]