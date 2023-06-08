// Runtime - 77.2% and Memory 86.10%

var singleNumber = function(nums) {
    let check = 0
    for (let i=0; i < nums.length; i++) {
        check = check ^ nums[i]
    }
    return check
};