// Doesnt work for horizontal lines

var checkStraightLine = function(coordinates) {
    let deltaY = (coordinates[0][1] - coordinates[1][1])
    let deltaX = (coordinates[0][0]-coordinates[1][0])
    let m = deltaY/deltaX
    let b = coordinates[0][1] - m*coordinates[0][0]
    for (let i = 2; i < coordinates.length; i++) {
        if (deltaX === 0) {
            if (coordinates[i][0] !== coordinates[coordinates.length-1][0]) {
                return false
            } else {
                return true
            }
        }
        if (coordinates[i][1] !== (m*coordinates[i][0] + b)) {
            return false
        }
    }
    return true
};