def sweetAndSavory(dishes, target):
    # Write your code here.
    dishes.sort()
    best = float("inf")
    best_l = 0
    best_r = 0
    l = 0
    r = len(dishes) - 1
    if not dishes or dishes[0] > 0:
        return [0, 0]
    while l < r:
        if dishes[l] > 0:
            break
        cur = dishes[l] + dishes[r]
        if cur > target:
            r -= 1
        if cur <= target and abs(target - cur) < best:
            best = cur
            best_l, best_r = dishes[l], dishes[r]
        l += 1
        
    return [best_l, best_r]
