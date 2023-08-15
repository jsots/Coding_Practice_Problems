"use strict";
// const a = [];
// This is not an array 
Object.defineProperty(exports, "__esModule", { value: true });
exports.bs_list = exports.linear_search = void 0;
// function sum_char(n: string): number {
//     let sum = 0;
//     for (let i = 0; i < n.length; ++i) {
//         for (let j = 0; j < n.length; ++j) {
//             sum += charCode;
//         }
//     }
//     return sum
// }
function linear_search(haystack, needle) {
    for (var i = 0; i < haystack.length; ++i) {
        if (haystack[i] === needle) {
            return true;
        }
    }
    return false;
}
exports.linear_search = linear_search;
console.log(linear_search([1, 2, 3], 2));
function bs_list(haystack, needle) {
    var lo = 0;
    var hi = haystack.length;
    do {
        var m = Math.floor(lo + (hi - lo) / 2);
        var v = haystack[m];
        if (v === needle) {
            return true;
        }
        else if (v > needle) {
            hi = m;
        }
        else {
            lo = m + 1;
        }
    } while (lo < hi);
    return false;
}
exports.bs_list = bs_list;
console.log(bs_list([1, 2, 3, 4, 5, 6], 5));
