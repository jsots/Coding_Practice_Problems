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

console.log(findClosestNumber([-4,-2,1,4,8]))