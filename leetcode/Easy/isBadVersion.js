var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let left = 0
        let right = n
        let mid = Math.floor((left + right)/2)
        while (left !== right) {
            if (isBadVersion(mid)) {
                right = mid
            } else {
                left = mid
            }
        }
    };
};




console.log(solution(5))