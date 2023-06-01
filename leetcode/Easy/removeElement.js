var removeElement = function(nums, val) {
    let ans = []
    let k = 0
    for (let j = 0; j < nums.length; j++) {
      if (nums[j] !== val) {
          ans.push(nums[j])
          k++
        } 
    }
    for (let i = 0; i<ans.length; i++) {
        nums[i] = ans[i]
    }
    return k;
};

// Below solution improves the memory but worsens the run time. run becomes 25.83 and memory becomes 91.61

var removeElement2 = function(nums, val) {
    let ans = []
    for (let j = 0; j < nums.length; j++) {
      if (nums[j] !== val) {
          ans.push(nums[j])
        } 
    }
    for (let i = 0; i<ans.length; i++) {
        nums[i] = ans[i]
    }
    return ans.length;
};