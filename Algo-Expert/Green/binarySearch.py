def binarySearch(array, target):
    # Write your code here.
    l = 0
    r = len(array) - 1
    while l < r:
        mid = (l + r) // 2
        if array[mid] > target:
            r = mid
        elif array[mid] < target:
            l = mid + 1
        else:
            l = r = mid
            return mid
    print(l)
    if array[l] != target:
        return -1