"use strict";
// const a = [];
// This is not an array 
Object.defineProperty(exports, "__esModule", { value: true });
exports.two_crystal_balls = exports.bs_list = exports.linear_search = void 0;
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
// Two Crystal Ball Problem
// Given two crystal balls that will break if dropped from high enough
// distance, determine the exact spot in which it will break in the most
// optimized way.
function two_crystal_balls(breaks) {
    var jmpAmount = Math.floor(Math.sqrt(breaks.length));
    var i = jmpAmount;
    for (; i < breaks.length; i += jmpAmount) {
        if (breaks[i]) {
            break;
        }
    }
    i -= jmpAmount;
    for (var j = 0; j < jmpAmount && i < breaks.length; ++j, ++i) {
        if (breaks[i]) {
            return i;
        }
    }
    return -1;
}
exports.two_crystal_balls = two_crystal_balls;
var test1 = [false, false, false, false, true, true, true, true, true, true, true, true];
console.log(two_crystal_balls(test1)); // Expected output: 4
var test2 = [false, false, false, false, false, false, false, true, true, true, true, true];
console.log(two_crystal_balls(test2)); // Expected output: 7
