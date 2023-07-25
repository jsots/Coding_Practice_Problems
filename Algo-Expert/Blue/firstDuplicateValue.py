def firstDuplicateValue(array):
    # Write your code here.
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1