// Runtime - 62.87% and Memory - 57.66%

var generate = function(numRows) {
    let triangle = []

    for (let i = 0; i <= numRows-1; i++) {
        let row = new Array(i+1).fill(0)
        row [0] = 1
        row [i] = 1

        for (let j = 1; j < i; j++) {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }

        triangle.push(row);
    }
    return triangle
};