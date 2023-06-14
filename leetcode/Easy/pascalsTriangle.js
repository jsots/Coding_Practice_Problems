var generate = function(numRows) {
    let rowOne = [1]
    let triangle = [[1]]

    for (let i = 2; i <= numRows; i++) {
        let prevRow = rowOne
        let nextRow = new Array(i).fill(0)
        for (let j = 0; j < nextRow.length; j++) {
            nextRow[j] = prevRow[j-1] + prevRow[j]
            triangle.push(nextRow)
            prevRow = nextRow
        }
    }
    return triangle
};