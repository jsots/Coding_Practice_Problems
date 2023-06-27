var moveZeroes = function(nums) {
    let j = 0
    for (let i = 0; i < nums.length-1; i++) {
        if (nums[i] === 0) {
            let temp = nums[i]
            j++
            nums[i] = nums[j]
            nums[j] = temp
        }
    }
    return nums
};

console.log(moveZeroes([0,1,0,3,12]))