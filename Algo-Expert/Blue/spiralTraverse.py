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
    r_min, r_max = 0, len(array) - 1 
    c_min, c_max = 0, len(array[0]) - 1 
    max_steps = (len(array)) * (len(array[0]))

    spiral_traverse = []
    steps = 0

    while steps < max_steps:
        for right in range(c_min, c_max + 1):
            spiral_traverse.append(array[r_min][right])
            steps += 1
        r_min += 1
        if steps >= max_steps:
            break
        for down in range(r_min, r_max + 1):
            spiral_traverse.append(array[down][c_max])
            steps += 1
        c_max -= 1
        if steps >= max_steps:
            break
        for left in range(c_max, c_min - 1, -1):
            spiral_traverse.append(array[r_max][left])
            steps += 1
        r_max -= 1
        if steps >= max_steps:
            break
        for up in range(r_max, r_min - 1, -1):
            spiral_traverse.append(array[up][c_min])
            steps += 1
        c_min += 1


    return spiral_traverse

