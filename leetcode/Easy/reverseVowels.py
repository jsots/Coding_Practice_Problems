class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        l = 0
        r = len(s) - 1
        new = [char for char in s]

        while l < r:
            if new[l].lower() not in vowels:
                l += 1
            else:
                if new[r].lower() in vowels:
                    tmp = new[l]
                    new[l] = new[r]
                    new[r] = tmp
                    r -= 1
                    l += 1
                else:
                    while new[r].lower() not in vowels:
                        r -= 1
        

        return "".join(new)