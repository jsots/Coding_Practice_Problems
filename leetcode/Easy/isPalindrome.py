# Runtime - 80.85% and Memory - 34.67%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = 0
        xString = str(x)
        right = len(xString)-1

        while left < right:
            if xString[left] == xString[right]:
                left+=1
                right-=1
            else:
                return False
        return True