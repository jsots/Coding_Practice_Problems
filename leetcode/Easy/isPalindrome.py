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


# Trying again:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0
        while i < j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() == s[j].lower():
                        i+=1
                        j-=1
                    else:
                        return False
                else:
                    j-=1
            else:
                i+=1
        return True



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            print("i:", s[i], "j:", s[j])
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1 
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
        
        return True