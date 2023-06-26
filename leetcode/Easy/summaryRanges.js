var summaryRanges = function(nums) {
    let startOfRange = 0
    let endOfRange = 0 
    let ranges = []
    for (let i = 0; i < nums.length; i++) {
        startOfRange = nums[i]
        let j = 0
        while (nums[j] + 1 === nums[j+1]) {
            j++
        }
        endOfRange = nums[j]
        ranges.push(`${startOfRange}->${endOfRange}`)
    }
    return ranges
};

console.log(summaryRanges([0,1,2,4,5,7]))