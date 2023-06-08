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

// Runtime - 47.82% and Memory = 24.73%

var majorityElement = function(nums) {
    let counter = 0
    let maxCounter = 0
    let maxNumber = 0
    nums.sort()
    if (nums.length === 1) {
        return nums[0]
    }
    for (let i=0; i < nums.length-1; i++) {
        if (nums[i] === nums[i+1]){
            counter += 2
            if (counter > maxCounter) {
                maxCounter = counter
                maxNumber = nums[i]
            }
        } else {
            counter = 0
        }
    }
    return maxNumber
};

// Runtime = 96.8% and Memory = 21.54%

var majorityElement = function(nums) {
    let counter = 0
    let maxCounter = 0
    let maxNumber = 0
    let end = nums.length-1
    nums.sort()
    if (nums.length === 1) {
        return nums[0]
    }
    for (let i=0; i < end; i++) {
        let current = nums[i]
        let next = nums[i+1]
        if (current === next){
            counter += 2
            if (counter > maxCounter) {
                maxCounter = counter
                maxNumber = nums[i]
            }
        } else {
            counter = 0
        }
    }
    return maxNumber
};

// Runtime - 98.16% and Memory - 98.43%
// Boyer-Moore Voting Algorithm

const majorityElement = function(nums) {
    let count = 0;

    let candidate = null;

    for (let i = 0; i < nums.length; i++) {
        if (count === 0) {
            candidate = nums[i];
        }

        count += nums[i] === candidate ? 1 : -1;
    }

    return candidate;
};