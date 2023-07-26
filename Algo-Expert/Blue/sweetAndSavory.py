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
        if dishes[r] < 0:
            break
        cur = dishes[l] + dishes[r]
        if cur > target:
            r -= 1
        if cur <= target:
            if abs(target - cur) < best:
                best = abs(target - cur)
                best_l, best_r = dishes[l], dishes[r]
            l += 1
        if best == 0:
            break
        
    return [best_l, best_r]



# Another way to solve, using two separate arrays.

def sweetAndSavory(dishes, target):
    # Write your code here.
    sweets = [dish for dish in dishes if dish < 0]
    savories = [dish for dish in dishes if dish > 0]
    sweets.sort()
    savories.sort(reverse = True)

    print(savories)

    best_pair = [0, 0]
    best_diff = float("inf")
    sweet_idx, savory_idx = 0, 0

    if not sweets or not savories:
        return best_pair

    while sweet_idx < len(sweets) and savory_idx < len(savories):
        cur = sweets[sweet_idx] + savories[savory_idx]

        if cur <= target:
            if abs(target - cur) < best_diff:
                best_diff = abs(target - cur)
                best_pair = [sweets[sweet_idx], savories[savory_idx]]
            sweet_idx += 1
        else:
            savory_idx += 1
            
    return best_pair

