function isPrime (num) {
    let mid = num/2
    if (num < 2) {
        return true
    }
    for (let i = 2; i <= mid; i++) {
        if (num % i === 0) {
            return false
        }
    }
    return true
}

console.log(isPrime(7))
console.log(isPrime(23))
console.log(isPrime(2))
console.log(isPrime(1))
console.log(isPrime(44))