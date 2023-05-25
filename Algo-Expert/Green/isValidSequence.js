function isValidSubsequence(arr, seq) {
  // Write your code here.
  let arrIdx = 0;
  let seqIdx = 0;
  while (arrIdx < arr.length && seqIdx < seq.length) {
    if (arr[arrIdx] === seq[seqIdx]) seqIdx ++;
    arrIdx++
  }
  return seqIdx === seq.length;
}
  
  let array2 = [5, 1, 22, 25, 6, -1, 8, 10]
  let sequence = [1, 6, -1, 10]
  
  console.log(isValidSubsequence(array2, sequence))