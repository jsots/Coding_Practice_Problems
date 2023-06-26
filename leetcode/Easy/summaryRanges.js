// Runtime - 72.45% and Memory 27.69%

var summaryRanges = function(nums) {
    let startOfRange = 0
    let endOfRange = 0 
    let ranges = []
    for (let i = 0; i < nums.length; i++) {
        startOfRange = nums[i]
        let j = i
        while (nums[j] + 1 === nums[j+1]) {
            j++
        }
        endOfRange = nums[j]
        if (startOfRange !== endOfRange) {
            ranges.push(`${startOfRange}->${endOfRange}`)
        } else {
            ranges.push(`${startOfRange}`)
        }
        i=j
    }
    return ranges
};

console.log(summaryRanges([0,1,2,4,5,7]))


// Runtime - 89.25% and Memory 97.14%

var summaryRanges = function(nums) {
    const result = [];

    let a = nums[0];

    for(let i = 0; i < nums.length; i++){
        if(i == nums.length || nums[i] + 1 != nums[i + 1]){
            if(a == nums[i]){
                result.push(a.toString());
            }else{
                result.push(`${a}->${nums[i]}`);
            }

            a = nums[i + 1];
        }
    }

    return result;    
};