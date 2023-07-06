class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        seen = {}
        j = 0
        i = j + 1
        while j < len(strs) - 1:
            temp = []
            while i < len(strs) - 1:
                if strs[j] not in anagrams:
                    i += 1
                    temp.append(strs[j])
                    if self.isAnagram(strs[i], strs[j]):
                        anagrams.append(strs[i])
            if temp:
                anagrams.append(temp)
            j += 1
            i = j
    
    def isAnagram(self, word_1, word_2):
        seen = {}
        if len(word_1) != len(word_2):
            return False
        for char in word_1:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
        for char in word_2:
            if char in seen:
                if seen[char] == 0:
                    seen[char] -= 1
            else:
                return False
        return True