function isValidSequence(arr, seq) {
    let c = 0
    for (let i=0; i < arr.length; i++) {
      if (seq.includes(arr[i])) {
        c++
      }
    }
    if (c === seq.length) {
      return true
    } else {
      return false
    }
  }
  
  let array2 = [5, 1, 22, 25, 6, -1, 8, 10]
  let sequence = [1, 6, -1, 10]
  
  console.log(isValidSequence(array2, sequence))