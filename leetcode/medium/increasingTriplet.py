class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        idxes = []
        numss = []
        for i, num in enumerate(nums):
            print(idxes, numss)
            if numss:
                if num <= numss[-1]:
                    idxes.pop()
                    numss.pop()
                    idxes.append(i)
                    numss.append(num)
                else:
                    idxes.append(i)
                    numss.append(num)
            else:
                idxes.append(i)
                numss.append(num)
            if len(idxes) == 3:
                return True
        return False