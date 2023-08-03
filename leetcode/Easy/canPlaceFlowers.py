class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1

        if len(flowerbed) == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n -= 1
                
        for i in range(1, len(flowerbed) - 1):
            prev = flowerbed[i - 1]
            cur = flowerbed[i]
            nxt = flowerbed[i + 1]

            if prev == 0 and cur == 0 and i == 1:
                flowerbed[i - 1] = 1
                n -= 1

            if cur == 0 and nxt == 0 and i == len(flowerbed) - 2:
                flowerbed[i + 1] = 1
                if n:
                    n -= 1

            if prev == 0 and cur == 0 and nxt == 0:
                if n:
                    n -= 1
                flowerbed[i] = 1
        
        if n:
            return False
        else:
            return True