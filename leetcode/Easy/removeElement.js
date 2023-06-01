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