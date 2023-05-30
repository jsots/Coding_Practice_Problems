let findLengthOfLCIS = function(nums) {
    let lCIS = []
    let ans = 1
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i-1]) {
            if (lCIS.length === 0) {
                lCIS.push(nums[i-1])
            }
            lCIS.push(nums[i])
        } else {
            if (lCIS.length > ans) {
                ans = lCIS.length
            }
            lCIS = []
        }
    }
    if (lCIS.length > ans) {
        return lCIS.length
    } else {
        return ans
    }
}

nums = [1,3,5,4, 7]
console.log(findLengthOfLCIS(nums))