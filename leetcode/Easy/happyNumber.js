/*
rite an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
*/

var isHappy = function(n) {
    // Create a hash set to keep track of the values we generate. Don't want duplicates, that will be a loop. 

    let visit = new Set()

    while (!visit.has(n)) {
        // So long as n has not been visited, keep going. 
        visit.add(n)
        // This adds n to the set.
        n = sumOfDigitsSquared(n)
        //  Finds the sum of the squared digits and sets n to that.

        if (n === 1) {
            // if n ever equals 1, we are done. this is simply true.
            return true
        }
    }
    // In the case that we visit a value twice, then we exit the loop. This means it is false because the value wasn't 1. 
    return false
};

// Below will handle the sum of squares for the digits. 
let sumOfDigitsSquared = function(n) {
    // Start with 0
    ans = 0

    // While n > 0, we will perform the following:
    while (n > 0) {
        // Lets get a way to grab the digit. Mod by 10 to obtain the one's place value. 
        let digit = n % 10;
        // Now we must multiply the ones digit by itself, and this will get added to the answer or the sum of the digits. 
        digit = digit ** 2
        ans += digit

        // Now we must divide by 10 and obtain the floor. This is akin to integer division in other languages. This will give us the integer that remains when we divide by 10 and reset the value of n to this. THen we go through the loop again. In a situation where it is 0, we break out! 
        n = Math.floor(n/10)
    }

    // Return the sum.
    return ans
}