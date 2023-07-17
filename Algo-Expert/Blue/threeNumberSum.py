def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    ans = []

    for i in range(len(array)-1):
        target = targetSum - array[i]
        j = i + 1
        k = len(array) - 1
        while j < k:
            if array[j] + array[k] > target:
                k -= 1
            elif array[j] + array[k] < target:
                j += 1
            else:
                ans.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
    return ans
