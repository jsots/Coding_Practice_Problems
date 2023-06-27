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

// Runtime - 87.97% and Memory - 64.47%

var canWinNim = function(n) {
    return n%4!==0
};