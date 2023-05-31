let isPalindrom = function(x) {
    let left = 0
    let s = x.toString()
    let right = s.length -1
    while (left < right) {
        if (s.charAt(left) === s.charAt(right)) {
            left ++
            right --
        } else {
            return false
        }
    }
    return true
}

console.log(isPalindrom(121))