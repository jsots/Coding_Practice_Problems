class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set()
        set_2 = set()
        ans_1 = []
        ans_2 = []
        ans = []

        for i in range(0, len(nums1)):
            set_1.add(nums1[i])
        for i in range(0, len(nums2)):
            set_2.add(nums2[i])
        
        unique_1 = set_1.difference(set_2)
        unique_2 = set_2.difference(set_1)

        for num in unique_1:
            ans_1.append(num)
        for num in unique_2:
            ans_2.append(num)
        
        ans.append(ans_1)
        ans.append(ans_2)
        
        return ans
