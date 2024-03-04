# Questions:
# Are negative numbers being used?
# How should i handle only one row or one column?
# Is an empty matrix a valid input?
# How do i handle when there are no lucky numbers?
# Should I assume that the input matrix will always be valid, or do I need to perform any validation checks?

# While loop to have a pointer that will go through the rows one by one
# Find the minimum in the row
# To find minimum, iterate through the entire row, set the min variable to the lowest value in that row
# THen, confirm it is a max to be a lucky number
# If it is not, then move to next row and repeat above
# All of this should take place in a while loop, where the cursor will check each row until there are no rows to check. Could also be a for loop, potentially
# Add to array of lucky numbers and this will become the answer


class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky = []

        for r in range(len(matrix)):
            r_min = float("inf")
            for c in range(len(matrix[r])):
                if r_min > matrix[r][c]:
                    r_min = matrix[r][c]
                    r_min_col = c
                    potential_lucky = r_min
            for r_2 in range(len(matrix)):
                potential_lucky = max(potential_lucky, matrix[r_2][r_min_col])
                print("potential----->", potential_lucky)
                print("r_min----->", r_min)
            if potential_lucky == r_min:
                lucky.append(r_min)
        
        return lucky

# O(n^2) for time
# O(n + m) for space


