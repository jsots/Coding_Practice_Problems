var missingNumber = function (nums) {
    nums.sort()
    let start = nums[0]
    let end = nums[nums.length-1]
    for ( let i = start; i < end; i++) {
        if (!nums.includes(i)) {
            return i
        }
    }
    if (nums.length ===1) {
        return start - 1
    }
    if (nums.length === 1 && nums[0] !== 0) {
        return start - 1
    }
    return end + 1
}

console.log(missingNumber([3, 0, 1]))