class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(1, len(flowerbed) - 2):
            prev = flowerbed[i - 1]
            cur = flowerbed[i]
            nxt = flowerbed[i + 1]

            if prev == 0 and cur == 0 and i == 1:
                flowerbed[i - 1] = 1
                n -= 1

            if cur == 0 and nxt == 0 and i == len(flowerbed) - 2:
                flowerbed[i + 1] = 1
                n -= 1

            if prev == 0 and cur == 0 and nxt == 0:
                n -= 1
                flowerbed[i] = 1
            
        
        if n:
            return False
        else:
            return True