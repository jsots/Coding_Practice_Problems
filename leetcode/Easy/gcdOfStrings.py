#still need to work on this

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisors = []
        divisor = ""
        i = 0
        while i < len(str1) and i < len(str2) and str1[i] == str2[i] and str1[i] not in divisors:
            divisors.append(str1[i])
            i += 1

        return "".join(divisors)