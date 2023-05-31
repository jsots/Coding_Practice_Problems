let twoSum = function(nums, target) {
    let ans = []
    for (let i=0; i<nums.length; i++) {
      for (let j=0; j<nums.length; j++) {
        if(i!==j && nums[i]+nums[j] === target) {
          ans.push(i)
        }
      }
    }
    return ans
};

console.log(twoSum([2,7,11,15]))