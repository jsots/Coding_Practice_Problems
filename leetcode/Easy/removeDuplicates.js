var removeDuplicates = function(nums) {
    for (let i=0; i<nums.length-1; i++) {
        if (nums[i] === nums[i+1]) {
            nums.splice(i,1)
            i--
        }
    }
    let k = nums.length
    return k
};

// Solution below has a better run time and memory. 

var removeDuplicates2 = function(nums) {
    let i = 0;
    for (let j = 1; j < nums.length; j++) {
      if (nums[i] !== nums[j]) {
        i++;
        nums[i] = nums[j];
      }
    }
    return i + 1;
  };