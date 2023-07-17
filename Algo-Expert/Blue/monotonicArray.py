def isMonotonic(array):
    # Write your code here.
    incr = False
    decr = False

    for i in range(1, len(array)):
        prev = i - 1
        curr = i
        if array[prev] > array[curr]:
            incr = True
            if decr:
                return False
        if array[prev] < array[curr]:
            decr = True
            if incr:
                return False

    return True
