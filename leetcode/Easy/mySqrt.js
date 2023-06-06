// Runtime 23.9% and Memory 90.69%

var mySqrt = function(x) {
    let i = 1
    while (i*i <= x) {
        i++
    }
    if (i*i === x) {
        return i
    }
    return i-1
};

// Runtime 98.55% and Memory 13.44%

var mySqrt = function(x) {
    if (x === 0) {
        return 0;
    }

    let left = 1;
    let right = x;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let sqr = mid * mid;

        if (sqr === x) {
            return mid;
        } else if (sqr < x) {
            left = mid +1;
        } else {
            right = mid -1;
        }
    }

    return right
};