var plusOne = function(digits) {
    for (let i = digits.length-1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i] += 1
            return digits
        } else if (i === 0) {
            digits[i] = 0
            digits.unshift(1)
        } else {
            digits[i] = 0
        }
    }
    return digits
};

console.log(plusOne([1,2,3]))