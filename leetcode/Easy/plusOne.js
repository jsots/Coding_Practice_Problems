var plusOne = function(digits) {
    let finalIndex = digits.length-1
    for (let i = finalIndex; i >= 0; i--) {
        let plusOneTarget = digits[i]
        if (plusOneTarget < 9) {
            plusOneTarget += 1
            return digits
        } else if (i === 0) {
            digits.unshift(1)
            plusOneTarget = 0
        } else {
            plusOneTarget = 0
        }
    }
    return digits
};

