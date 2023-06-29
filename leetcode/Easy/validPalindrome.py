class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if not isAlphaNumeric(s[left].lower()):
                left += 1
            if not isAlphaNumeric(s[right].lower()):
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left+=1
                right-=1
        return True


def isAlphaNumeric(string):
    code = ord(string)
    return (code >= 48 and code <= 57) or (code >= 65 and code <= 90) or (code >= 97 and code <= 122)