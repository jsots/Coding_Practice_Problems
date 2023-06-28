# Runtime - 90.92% and Memory - 13.66%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        for i in range(0, len(s)):
            if s[i] in left:
                stack.append(left.index(s[i]))
            if s[i] in right:
                if len(stack) == 0:
                    return False
                if stack[-1] == right.index(s[i]):
                    del stack[-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
            