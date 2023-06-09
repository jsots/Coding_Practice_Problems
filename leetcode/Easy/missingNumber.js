var missingNumber = function (nums) {
    nums.sort()
    for (let i = 0; i <= nums.length; i++) {
        if (!nums.includes(i)) {
            return i;
        }
    }
    if (nums.length > end) {
        return end + 1
    } else {
        return start - 1
    }
}

console.log(missingNumber([3, 0, 1]))