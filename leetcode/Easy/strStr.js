var strStr = function(haystack, needle) {
    if (haystack.includes(needle)) {
        let ans = haystack.indexOf(needle);
        return ans;
    }
    return -1
};


let haystack = "sadbutsad" 
let needle = "sad"
console.log(strStr(haystack, needle))