// Doesnt work for horizontal lines

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

// solution below

var checkStraightLine = function(coordinates) {
    coordLen = coordinates.length

    if(coordLen <= 2) return true

    function calculateSlope(x1, y1, x2, y2, x, y) {
    return (y2 - y1) * (x - x1) - (y - y1) * (x2 - x1);
  }

    let [x1, y1] = coordinates[0]
    let [x2, y2] = coordinates[1]

   for (let i = 2; i < coordinates.length; i++) {
    let [x, y] = coordinates[i];
    if (calculateSlope(x1, y1, x2, y2, x, y) !== 0) {
      return false;
    }
  }

  return true;
};