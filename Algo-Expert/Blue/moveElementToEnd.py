def moveElementToEnd(array, toMove):
    # Write your code here.
    temp = 0
    i = 0
    j = len(array) - 1

    while i < j:
        print(i, j)
        while array[j] == toMove and j > i:
            j -= 1
        if array[i] == toMove:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
        i += 1
        print(i, j)
        
    return array
