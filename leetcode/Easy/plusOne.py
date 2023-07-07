# Runtime - 91.80% and Memory 67.78%

# list comperehension solution that evan showed me

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_string = [str(digit) for digit in digits]
        digit_joined = int("".join(digits_string)) + 1
        result = [int(digit) for digit in str(digit_joined)]
        return result

# Solved below!!!

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = True
        reverse = list(reversed(digits))
        for i in range(len(digits)):
            if reverse[i] == 9 and carry:
                # do something
                ans.append(0)
            else:
                ans.append(reverse[i] +1) if carry else ans.append(reverse[i])
                carry = False
        if carry:
            ans.append(1)
        return reversed(ans)