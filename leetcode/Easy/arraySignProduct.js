// 36.67% runtime and 33.13% memory

var arraySign = function(nums) {
    let neg = []
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            return 0
        } else if (nums[i] < 0) {
            neg.push(nums[i])
        }
    }
    if (neg.length % 2 === 0) {
        return 1
    } else {
        return -1
    }
};