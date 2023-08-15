"use strict";
// const a = [];
// This is not an array 
Object.defineProperty(exports, "__esModule", { value: true });
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
exports.default = linear_search;
console.log(linear_search([1, 2, 3], 2));
