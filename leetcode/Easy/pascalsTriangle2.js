//

var getRow = function(rowIndex) {
    let triangle = []

    for (let i = 0; i <= rowIndex; i++) {
        let row = new Array(i+1).fill(0)

        row[0] = 1
        row[i] = 1

        for (let j=1; j < i; j++) {
            row[j] = row[i-1][j-1] + row[i-1][j]
        }

        triangle.push(row)
    }
    return triangle[triangle.length-1]
};