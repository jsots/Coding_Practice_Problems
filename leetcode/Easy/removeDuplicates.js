var removeDuplicates = function(nums) {
    let indeces = []
    for (let i=0; i<nums.length; i++) {
        if (nums[i] === nums[i+1]) {
            indeces.push(nums[i])
            i++
        }
        indeces.push(nums[i])
    }
    let k = indeces.length
    return k
};