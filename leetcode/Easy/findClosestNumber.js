var findClosestNumber = function(nums) {
    let shortestDistance = Infinity
    let ans = 0
    nums.sort()
    for (let i = 0; i < nums.length; i++) {
        let currentDistance = Math.abs(nums[i])
        if (currentDistance <= shortestDistance) {
            shortestDistance = currentDistance
            ans = nums[i]
        }
    }
    return ans
};

console.log(findClosestNumber([-4,-2,1,4,8]))