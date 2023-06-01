var removeDuplicates = function(nums) {
    for (let i=0; i<nums.length-1; i++) {
        if (nums[i] === nums[i+1]) {
            nums.splice(i,i+1)
        }
    }
    let k = nums.length
    return k
};