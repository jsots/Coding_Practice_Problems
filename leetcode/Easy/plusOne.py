# Runtime - 91.80% and Memory 67.78%

# list comperehension solution that evan showed me

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_string = [str(digit) for digit in digits]
        digit_joined = int("".join(digits_string)) + 1
        result = [int(digit) for digit in str(digit_joined)]
        return result