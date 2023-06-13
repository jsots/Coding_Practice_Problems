var checkStraightLine = function(coordinates) {
    let m = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
    let b = coordinates[0][1] - m*coordinates[0][0]
    for (let i = 2; i < coordinates.length; i++) {
        if (coordinates[i][1] !== (m*coordinates[i][0] + b)) {
            return false
        }
    }
    return true
};
};