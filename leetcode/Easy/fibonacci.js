// Runtime = 94.95% and Memory - 87.4%

var fib = function(n) {
    let fib = [1, 1]
    if (n === 0) {
        return 0
    } else if (n <= 2) {
        return 1
    }
    for (let i = 1; i <= n; i++) {
        let prev = fib[i-1]
        let current = fib[i]
        fib.push(current + prev)
    }
    return fib[n-1]
};