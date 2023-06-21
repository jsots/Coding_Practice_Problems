/*
rite an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
*/

var isHappy = function(n) {
    if (n < 10) {
        return false
    }
    let ans = 0
    let counter = 0
    while (ans !== 1 || counter > 50) {
        let onesDigit = n % 10
        let tensDigit = Math.floor(n/10)
        ans = (onesDigit**2) + (tensDigit**2)
        n = ans
        counter++
        if (counter === 50) {
            return false
        }
    }
    return true
};