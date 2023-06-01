// Below is 90.1% runtime and 31.74% memory.
var strStr = function(haystack, needle) {
    if (haystack.includes(needle)) {
        let ans = haystack.indexOf(needle);
        return ans;
    }
    return -1
};


// Below is 70.54% runtime & 75.35% memory
var strStr2 = function(haystack, needle) {
    if (!haystack.includes(needle)) {
        return -1
    }
    let ans = haystack.indexOf(needle);
    return ans;
};