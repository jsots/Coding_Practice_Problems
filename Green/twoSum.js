function twoSum(arr, int) {
    let ans = []
    for (let i=0; i<arr.length-1; i++) {
      for (let j=0; j<arr.length-1; j++) {
        if(i!==j && arr[i]+arr[j] === int) {
          ans.push(arr[i])
        }
      }
    }
    return ans
  }
  
  let array = [3, 5, -4, 8, 11, 1, -1, 6]
  let targetSum = 10
  
  console.log(twoSum(array, targetSum))