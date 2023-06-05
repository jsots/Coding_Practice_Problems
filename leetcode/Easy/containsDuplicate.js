// 12.83% runtime and 99.87% memory

var containsDuplicate = function(nums) {
    let len = nums.length
    for (let i = 0; i < len; i++) {
        for (let j = i+1; j < len; j++) {
            if (nums[i] === nums[j]) {
                return true
            }
        }
    }
    return false
};

// 63.29% runtime and 69.71% memory
var containsDuplicate2 = function(nums) {
    let numberCounter = {}
    for (let i = 0; i < nums.length; i++) {
        if (numberCounter[nums[i]]) {
            return true
        }
        numberCounter[nums[i]] = 1
    }
    return false
};