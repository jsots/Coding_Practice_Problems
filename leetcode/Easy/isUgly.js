// Runtime - 62.86% and Memory - 53.32%

var isUgly = function (n) {
    if(n <= 0) return false

    while (n != 1) {
        if (n % 2 === 0) {
            n /= 2
        } else if (n % 3 === 0) {
            n /= 3
        } else if (n % 5 === 0) {
            n /= 5
        } else {
            return false
        }
    }

    return true
};

console.log(isPrime(7))
console.log(isPrime(23))
console.log(isPrime(2))
console.log(isPrime(1))
console.log(isPrime(44))