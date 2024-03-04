# Find the minimum in the row
# To find minimum, iterate through the entire row, set the min variable to the lowest value in that row
# THen, confirm it is a max to be a lucky number
# If it is not, then move to next row and repeat above
# Add to array of lucky numbers and this will become the answer


class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        