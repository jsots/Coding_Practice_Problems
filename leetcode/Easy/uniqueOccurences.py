class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        unique = set()

        for num in arr:
            occurences[num] = 1 + occurences.get(num, 0)

        for occ in occurences.values():
            if occ in unique:
                return False
            else:
                unique.add(occ)
        
        return True