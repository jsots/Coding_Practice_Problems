class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_count = 0
        for i in range(0, len(s)):
            word = s[i:i+k]
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
                max_count = max(count, max_count)
        
        return max_count