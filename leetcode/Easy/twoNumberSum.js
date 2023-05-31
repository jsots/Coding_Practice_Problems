let twoSum = function(nums, target) {
    let ans = []
    let len = nums.length
    for (let i=0; i<len; i++) {
      for (let j=i+1; j<len; j++) {
        if(nums[i]+nums[j] === target) {
          ans.push(i)
          ans.push(j)
        }
      }
    }
    return ans
};

console.log(twoSum([2,7,11,15]))