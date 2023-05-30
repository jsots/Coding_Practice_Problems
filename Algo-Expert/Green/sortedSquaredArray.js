// Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order. 
function sortedSquaredArray(array) {
  // Write your code here.
  let sqrs = []
  let sqr = 0
    array.forEach((num) => {
      sqr = num**2
      sqrs.push(sqr)
    })
  return sqrs.sort(function(a, b){return a - b})
}

let array3 = [1, 2, 3, 5, 6, 8, 9]
console.log(sortedSquaredArray(array3))