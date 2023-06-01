var searchInsert = function(nums, target) {
    if (nums.includes(target)) {
        return nums.indexOf(target)
    } else if (target < nums[0]) {
        return 0
    } else if (target > nums[nums.length-1]) {
        return nums.length
    }
    for (let i=0; i<nums.length-1; i++) {
        if (target > nums [i] && target < nums[i+1]) {
            nums.splice(i, 0, target)
            return i+1
        }
    }
};