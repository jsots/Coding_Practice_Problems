class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        let words = s.split(" ")
        return len(words[-1])
