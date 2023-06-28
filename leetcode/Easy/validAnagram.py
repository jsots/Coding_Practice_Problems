# Runtime - 70.37% and Memory - 91.25%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        originalSet = {}
        for char in s:
            if char in originalSet:
                originalSet[char] += 1
            else:
                originalSet[char] = 1
        for char in t:
            if char in originalSet:
                originalSet[char] -= 1
                if originalSet[char] < 0:
                    return False
            else:
                return False
        return True


# Alt answer is sorting them, this is to not take up more memory:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Using the neetcode solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            # get will...get the key and otherwise set a default value
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True