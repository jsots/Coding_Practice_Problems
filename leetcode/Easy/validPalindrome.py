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


# Solved another day

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -= 1
                    else: 
                        return False
                else:
                    j -= 1
            else:
                i += 1

        return True