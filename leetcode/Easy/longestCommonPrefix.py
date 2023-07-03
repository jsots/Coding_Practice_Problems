class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            new_prefix = ""
            while j < len(strs[i]) and j < len(common_prefix) and strs[i][j] == common_prefix[j]:
                print(new_prefix)
                new_prefix += strs[i][j]
                j += 1
            common_prefix = new_prefix
        return common_prefix