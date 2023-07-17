def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # Are the arrays the same length?
    # This is a greedy style problem
    
    arrayOne.sort()
    arrayTwo.sort()
    pair = [0] * 3
    curr_min = float("inf")
    j = 0
    i = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        difference = abs(abs(arrayOne[i]) - abs(arrayTwo[j]))
        if curr_min > difference:
            curr_min = difference
            pair[1] = arrayOne[i]
            pair[2] = arrayTwo[j]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else: 
            j += 1 
        
    return [pair[1], pair[2]]
