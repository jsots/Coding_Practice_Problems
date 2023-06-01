var removeDuplicates = function(nums) {
    let indeces = []
    for (let i=0; i<nums.length; i++) {
        if (nums[i] === nums[i+1]) {
            indeces.push(i)
        }
    }
    for (let j = 0; j<indeces.length; j++) {
        nums.splice(indeces[j], indeces[j]+1)
    }
    let k = nums.length
    return k
};