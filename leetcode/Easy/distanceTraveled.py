class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        counter = 0
        if mainTank < 5:
            return mainTank * 10
        else:
            if additionalTank >= 1:
                while mainTank >= 5:
                    mainTank - 5
                    counter += 1
                return ((mainTank + 1) * 10 * counter
            else:
                while mainTank >= 5:
                    mainTank - 5
                    counter += 1
                return (mainTank * 10) * counter