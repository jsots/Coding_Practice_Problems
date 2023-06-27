var moveZeroes = function(nums) {
    let zeroes = []
    let nonZeroes = []
    nums.forEach( (num) => {
        if (num === 0) {
            zeroes.push(num)
        } else {
            nonZeroes.push(num)
        }
    })
    for (let i = 0; i < zeroes.length; i++) {
        nonZeroes.push(zeroes[i])
    }
    return nonZeroes
};

console.log(moveZeroes([0,1,0,3,12]))