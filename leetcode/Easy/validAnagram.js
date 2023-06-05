// Runtime - 45.49% and Memory - 16.69%

var isAnagram = function(s, t) {
    s = s.split("").sort().join("")
    t = t.split("").sort().join("")
    if (s === t) {
        return true
    }
    return false
};

// Runtime - 99.71% Memory - 92.29%

var isAnagram = function(s, t) {
    if (s.length !== t.length){
        return false;
    }

    const freq = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++) {
        const charCodeS = s.charCodeAt(i) - 97;
        const charCodeT = t.charCodeAt(i) - 97;

        freq[charCodeS]++;
        freq[charCodeT]--;
    }

    return freq.every((value) => value === 0);

}