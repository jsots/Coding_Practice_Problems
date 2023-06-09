var missingNumber = function (nums) {
    nums.sort()
    let end = nums.length
    for (let i = 0; i <= end; i++) {
        if (!nums.includes(i)) {
            return i;
        }
    }
}

console.log(missingNumber([3, 0, 1]))