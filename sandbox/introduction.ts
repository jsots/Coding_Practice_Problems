// const a = [];
// This is not an array 

// function sum_char(n: string): number {
//     let sum = 0;
//     for (let i = 0; i < n.length; ++i) {
//         for (let j = 0; j < n.length; ++j) {
//             sum += charCode;
//         }
//     }
//     return sum
// }


export function linear_search(haystack: number[], needle: number): boolean {

    for (let i = 0; i < haystack.length; ++i) {
        if (haystack[i] === needle) {
            return true;
        }
    }

    return false;
}
console.log(linear_search([1,2,3], 2))


export function bs_list(haystack: number[], needle: number): boolean {

    let lo = 0;
    let hi = haystack.length;
    do {
        const m = Math.floor(lo + (hi - lo) / 2);
        const v = haystack[m];

        if (v === needle) {
            return true;
        } else if (v > needle) {
            hi = m;
        } else {
            lo = m + 1;
        }
    } while (lo < hi);

    return false;
}

console.log(bs_list([1,2,3,4,5,6], 5))


// Two Crystal Ball Problem

// Given two crystal balls that will break if dropped from high enough
// distance, determine the exact spot in which it will break in the most
// optimized way.

export function two_crystal_balls(breaks: boolean[]): number {
    const jmpAmount = Math.floor(Math.sqrt(breaks.length));

    let i = jmpAmount;
    for (; i < breaks.length; i += jmpAmount) {
        if (breaks[i]) {
            break;
        }
    }

    i -= jmpAmount;

    for (let j = 0; j < jmpAmount && i < breaks.length; ++j, ++i) {
        if (breaks[i]) {
            return i;
        }
    }

    return -1
}

const test1 = [false, false, false, false, true, true, true, true, true, true, true, true];
console.log(two_crystal_balls(test1));  // Expected output: 4

const test2 = [false, false, false, false, false, false, false, true, true, true, true, true];
console.log(two_crystal_balls(test2));  // Expected output: 7
