// Bubble sort

// O(n^2) bc it's (n(n+1))/2

export function bubble_sort(arr: number[]): void {
    for (let i = 0; i < arr.length; ++i) {
        for (let j = 0; j < arr.length - 1 - i; ++j) {
            if (arr[j] > arr[j+1]) {
                const tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j + 1] = tmp
            }
        }
    }
}

// Test case 1: Basic test case with small array
const testArray1 = [4, 2, 7, 1, 5];
bubble_sort(testArray1);
console.log(testArray1); // Expected output: [1, 2, 4, 5, 7]

// Test case 2: Large array with descending order
const testArray2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
bubble_sort(testArray2);
console.log(testArray2); // Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Test case 3: Array with repeated elements
const testArray3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
bubble_sort(testArray3);
console.log(testArray3); // Expected output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]