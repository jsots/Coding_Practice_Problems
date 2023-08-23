class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        idxes = []
        numss = []
        for i, num in enumerate(nums):
            if numss:
                if num <= numss[-1]:
                    if len(nums) - i > len(numss):
                        idxes.pop()
                        numss.pop()
                        if numss:
                            if num <= numss[-1]:
                                if len(nums) - i > len(numss):
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
            print(idxes, numss)
            if len(idxes) == 3:
                return True
        return False