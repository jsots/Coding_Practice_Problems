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

// 75.23% runtime and 58.92% memory
var arraySign2 = function(nums) {
    let product = 1
    let containsZero = false
    let signFunc = Math.sign
    nums.forEach((num) => {
        if (num === 0) {
            containsZero = true
        }
        product *= num
    })

    if (containsZero) {
        return 0
    }
    return signFunc(product)
};