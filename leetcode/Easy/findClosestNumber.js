var findClosestNumber = function(nums) {
    let shortestDistance = Infinity
    let ans = 0
    nums.sort()
    for (let i = 0; i < nums.length; i++) {
        let currentDistance = Math.abs(nums[i])
        if (currentDistance <= shortestDistance) {
            shortestDistance = currentDistance
            ans = nums[i]
        }
    }
    return ans
};

console.log(findClosestNumber([-4,-2,1,4,8]))

// Runtime - 68.53% and Memory 79.2% 

var findClosestNumber = function(nums) {
    let pos = Infinity;
    let neg = -Infinity
 
    for(let i=0; i<nums.length;i++) {
        if(nums[i] > 0) {
            if(pos > nums[i])
            pos = nums[i]
        } else {
            if(neg < nums[i]) 
             neg = nums[i]
            }
        
    }
 
        if(-neg < pos) {
            return neg;
        }
        return pos;
    
 };