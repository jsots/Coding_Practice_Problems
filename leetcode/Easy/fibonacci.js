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

// Runtime 82.80% and Memory - 87.4%

var fib = function(n) {
    let a = 0
    let b = 1
    let c = 1
    let count = 2
    if (n === 0 || n === 1) {
        return n
    } else {
        while (count <= n) {
            c = a + b
            a = b
            b = c
            count++
        }
    }
    return c
};