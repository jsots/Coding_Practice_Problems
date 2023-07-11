class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        start = 0
        end = k
        beauty_int = 0
        while end <= len(num):
            if int(num[start:end]):
                print(int(num[start:end]))
                if int(num) % int(num[start:end]) == 0:
                    beauty_int += 1
            start += 1
            end += 1
        
        return beauty_int