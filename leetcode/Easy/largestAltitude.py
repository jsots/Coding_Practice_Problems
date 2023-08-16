class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = 0
        cur_alt = 0

        for i in range(0, len(gain)):
            cur_alt += gain[i]
            highest_alt = max(cur_alt, highest_alt)

        return highest_alt