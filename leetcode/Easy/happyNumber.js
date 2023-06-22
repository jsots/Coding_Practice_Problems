/*
rite an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
*/

var isHappy = function(n) {
    let visit = new Set()

    while (!visit.has(n)) {
        visit.add(n)
        n = sumOfDigitsSquared(n)

        if (n === 1) {
            return true
        }
    }
    return false
};

let sumOfDigitsSquared = function(n) {
    ans = 0
    while (n > 0) {
        let digit = n % 10;
        digit = digit ** 2
        ans += digit
        n = Math.floor(n/10)
    }
    return ans
}