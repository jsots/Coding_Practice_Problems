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

// Runtime - 37.21% and Memory - 60.57%

var isPowerOfTwo = function(n) {
    let check = 1
    if (n > 1 && n % 2 !== 0) {
        return false
    }
    while (check <= n) {
        if (n === check) {
            return true
        }
        check *= 2
    }
    return false
};

// Runtime - 68.90% and Memory - 31.26%

var isPowerOfTwo = function(n) {
    if (n > 1 && n % 2 !== 0) {
        return false
    }
    while (n >= 1) {
        if (n === 1) {
            return true
        }
        n /= 2
    }
    return false
};

// Runtime 43.16% and Memory 60.57%

var isPowerOfTwo = function(n) {
    let check = 1
    while (n >= check) {
        if (n === check) {
            return true
        }
        n /= 2
    }
    return false
};

// Runtime 57.87% and Memory - 76.96%

var isPowerOfTwo = function (n) {
    if (n === 1) return true;
    if (n <= 0) return false;
    if (n % 2 !== 0) return false;
    return isPowerOfTwo(n / 2);
};