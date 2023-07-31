class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        div_1 = []
        div_2 = []
        for char in str1:
            if char not in div_1:
                div_1.append(char)
        for char in str2:
            if char not in div_2:
                div_2.append(char)
        
        if div_1 != div_2:
            return ""
        else:
            return "".join(div_1)