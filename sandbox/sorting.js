"use strict";
// Bubble sort
Object.defineProperty(exports, "__esModule", { value: true });
exports.bubble_sort = void 0;
// O(n^2) bc it's (n(n+1))/2
function bubble_sort(arr) {
    for (var i = 0; i < arr.length; ++i) {
        for (var j = 0; j < arr.length - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                var tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}
exports.bubble_sort = bubble_sort;
// Test case 1: Basic test case with small array
var testArray1 = [4, 2, 7, 1, 5];
bubble_sort(testArray1);
console.log(testArray1); // Expected output: [1, 2, 4, 5, 7]
// Test case 2: Large array with descending order
var testArray2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
bubble_sort(testArray2);
console.log(testArray2); // Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// Test case 3: Array with repeated elements
var testArray3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
bubble_sort(testArray3);
console.log(testArray3); // Expected output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
