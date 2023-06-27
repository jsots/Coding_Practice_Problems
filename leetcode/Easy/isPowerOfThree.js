// Runtime - 78.86% And Memory - 59.33%

var isPowerOfThree = function(n) {
    if (n === 1) {
        return true
    } else if (n % 3 !== 0 || n <= 0) {
        return false
    }
    return isPowerOfThree(n/3)
};

console.log(isPowerOfThree(27))

// Even cleaner way below

var isPowerOfThree = function(n) {
    if(n===0) return false
    if(n===1) return true
    if(n%3 ===0) return isPowerOfThree(Math.floor(n/3))
    else return false

};