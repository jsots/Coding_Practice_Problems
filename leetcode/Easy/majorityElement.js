// Runtime - 10.50% and Memory - 56.20%

var majorityElement = function(nums) {
    let numberCounter = {}
    for (let i=0; i<nums.length; i++) {
        numberCounter[nums[i]] ? numberCounter[nums[i]] ++ : numberCounter[nums[i]] = 1
    }
    let max = -Infinity
    let majorityElement = 0
    for (let key in numberCounter) {
        if (numberCounter[key] > max) {
            max = numberCounter[key]
            majorityElement = key
        }
    }
    return majorityElement
};