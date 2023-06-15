// Runtime - 48.73% and Memory - 31.26%

var isPowerOfTwo = function(n) {
    if (n  === 1) {
        return true
    } else if (n % 2 !== 0) {
        return false
    }
    let check = 2
    while (check <= n) {
        if (n === check) {
            return true
        }
        check *= 2
    }
    return false
};