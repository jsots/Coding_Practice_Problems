class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank < 5:
            return mainTank * 10
        else:
            if additionalTank >= 1:
                return (mainTank + 1) * 10
            else:
                return mainTank * 10