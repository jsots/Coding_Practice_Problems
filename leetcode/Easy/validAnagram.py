#

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        originalSet = {}
        anagramSet = {}
        if len(s) != len(t):
            return False
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