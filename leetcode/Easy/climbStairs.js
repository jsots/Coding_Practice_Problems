var climbStairs = function(n) {
    let ans = 0
    if (n === 2) {
        return 2
    }
    if (n % 2 === 0) {
        ans = 2 + (n-1) + (n-2)*(n-4)
        return ans
    } else {
        ans = 1 + (n-1) + (n-2)*(n-4)
        return ans
    }
};