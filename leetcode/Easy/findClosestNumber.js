var findClosestNumber = function(nums) {
    let shortestDistance
    for (let i = 0; i < nums.length; i++) {
        let currentDistance = nums[i]
        if (currentDistance < shortestDistance) {
            shortestDistance = currentDistance
        }
    }
    return shortestDistance
};