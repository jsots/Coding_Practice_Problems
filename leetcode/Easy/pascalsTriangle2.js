// Runtime - 94.7% and Memory - 62.61%

var getRow = function(rowIndex) {
    let triangle = []

    for (let i = 0; i <= rowIndex; i++) {
        let row = new Array(i+1).fill(0)

        row[0] = 1
        row[i] = 1

        for (let j=1; j < i; j++) {
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        }

        triangle.push(row)
    }
    return triangle[rowIndex]
};