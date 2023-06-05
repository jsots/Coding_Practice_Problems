// Runtime - 45.49% and Memory - 16.69%

var isAnagram = function(s, t) {
    s = s.split("").sort().join("")
    t = t.split("").sort().join("")
    if (s === t) {
        return true
    }
    return false
};