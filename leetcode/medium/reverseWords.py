
class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        words = []
        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1
            
            if i < len(s):
                word = []
                while i < len(s) and s[i] != " ":
                    word.append(s[i])
                    i += 1
                words.append("".join(word))
                i += 1  # Skip over the space after the word if it exists
        
        return " ".join(reversed(words))


# alt solution:

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
