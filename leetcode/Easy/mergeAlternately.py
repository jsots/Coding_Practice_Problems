class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        if len(word1) >= len(word2):    
            for i in range(len(word2)):
                ans.append(word1[i])
                ans.append(word2[i])
            ans.append(word1[i+1:])
        else:
            for i in range(len(word1)):
                ans.append(word1[i])
                ans.append(word2[i])
            ans.append(word2[i+1:])
        
        return "".join(ans)