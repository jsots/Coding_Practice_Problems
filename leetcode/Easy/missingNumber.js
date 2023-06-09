var missingNumber = function (nums) {
    nums.sort()
    let start = nums[0]
    let end = nums[nums.length-1]
    for ( let i = start; i < end; i++) {
        if (!nums.includes(i)) {
            return i
        }
    }
}

console.log(missingNumber([3, 0, 1]))