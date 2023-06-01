// 31.67% runtime & 20.18% memory

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

// 60.69% runtime & 82.46% memory

var searchInsert2 = function(nums, target) {
    let lastIndex = nums.length-1
    let len = nums.length
    if (nums.includes(target)) {
        return nums.indexOf(target)
    } else if (target < nums[0]) {
        return 0
    } else if (target > nums[lastIndex]) {
        return len
    }
    for (let i=0; i<nums.length-1; i++) {
        if (target > nums [i] && target < nums[i+1]) {
            nums.splice(i, 0, target)
            return i+1
        }
    }
};

// 76.47% runtime & 66.27% memory

var searchInsert3 = function(nums, target) {
    let lastIndex = nums.length-1
    let len = nums.length
    if (target < nums[0]) {
        return 0
    } else if (target > nums[lastIndex]) {
        return len
    } else if (nums.includes(target)) {
        return nums.indexOf(target)
    }
    for (let i=0; i<nums.length-1; i++) {
        if (target > nums [i] && target < nums[i+1]) {
            nums.splice(i, 0, target)
            return i+1
        }
    }
};