// Below is 53.71% runtime and 40.98% memory.

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

// below is 68.37% runtime and 86.49% memory.

var removeElement2 = function(nums, val) {
    let ans = []
    let k = 0
    for (let j = 0; j < nums.length; j++) {
      if (nums[j] !== val) {
          ans.push(nums[j])
          k++
        } 
    }
    for (let i = 0; i<k; i++) {
        nums[i] = ans[i]
    }
    return k;
};