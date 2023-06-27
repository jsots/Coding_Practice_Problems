// Runtime - 17.77% and Memory - 42.12%

var canWinNim = function(n) {
    if (n < 4) {
        return true
    } else if (n % 4 === 0) {
        return false
    }
    return true
};

console.log(canWinNim(4))