# How do I handle null?
# How do I handle an invalid entry, should I have a validation check for a matrix input?
# What if it is 1 x 1?
# Is empty a valid input?

# Iterate until all cells have been visited. Maybe keep track of this with a set?
# Could also keep track of max steps.
# Iterate through the row first, stopping at the end. Then, go down the column, then go backwards, then vert backwards, then reset. This will be repeated until completion. Reg, reg, reverse, reverse. 

# Keep track of answer in an array. Append the array as I visit each spot. 

def spiralTraverse(array):
    # Write your code here.
    r_min, r_max = 0, len(array)
    c_min, c_max = 0, len(array[0])
    max_steps = (len(array) + 1) * (len(array[0]) + 1)

    spiral_traverse = []
    for r in range(r_max):

    pass