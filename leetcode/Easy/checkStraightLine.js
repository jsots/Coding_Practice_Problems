// Runtime - 5.20% and Memory - 37.97%

var checkStraightLine = function(coordinates) {
    let deltaY = (coordinates[0][1] - coordinates[1][1])
    let deltaX = (coordinates[0][0]-coordinates[1][0])
    let m = deltaY/deltaX
    let b = coordinates[0][1] - m*coordinates[0][0]

    if (deltaX === 0) {
        for (let j = 0; j < coordinates.length-1; j++) {
            if (coordinates[j][0] !== coordinates[j+1][0]) {
                return false
            } 
        }
        return true
    }
    for (let i = 2; i < coordinates.length; i++) {
        if (coordinates[i][1] !== (m*coordinates[i][0] + b)) {
            return false
        }
    }
    return true
};

// better solution
var checkStraightLine = function(coordinates) {
    let grad;
    for (let i = 0, j = 1; j < coordinates.length; i++, j++) {
        let rise = coordinates[j][1] - coordinates[i][1];
        let run = coordinates[j][0] - coordinates[i][0];
        let currGrad;
        if (run == 0) currGrad = Infinity;
        else currGrad = rise / run;
        if (i > 0) {
            if (currGrad !== grad) return false;
        }
        grad = currGrad;
    }
    return true;
};