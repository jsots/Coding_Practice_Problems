class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        while len(words[-1]) == 0:
            words.pop()
        return len(words[-1])
