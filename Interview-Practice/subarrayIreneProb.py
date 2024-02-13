def subarray(array, length, value):    
    ans = 0
    l = 0

    for r in range(len(array) - 1):
        print("l -----", l)
        check = set()
        r = length - 1
        right = array[r]
        for l in range(r + 1):
            left = array[l]
            print("left ---", left)
            compliment = value - left
            print("compliment", compliment)
            if compliment in check:
                ans += 1
                break
            check.add(left)
        print("check set", check)
        print("current ans", ans)
        r += 1
        l += 1

    return ans

a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
m = 4
k = 10
print(subarray(a, m, k))
