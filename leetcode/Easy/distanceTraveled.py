class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        consumed = 0
        distance = 0
        if mainTank < 5:
            return mainTank * 10
        else:
            while mainTank > 0:
                consumed += 1
                mainTank -= 1
                distance += 10
                if consumed == 5:
                    consumed = 0
                    if additionalTank >= 1:
                        additionalTank -= 1
                        mainTank += 1
            return distance