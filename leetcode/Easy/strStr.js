var strStr = function(haystack, needle) {
    if (haystack.includes(`${needle}`)) {
        let ans = haystack.split(`${needle}`)
        for(let i= 0; i<ans.length; i++) {
            if (ans[i] === "") {
                return i
            }
        }
    }
    return -1
};


let haystack = "sadbutsad" 
let needle = "sad"
console.log(strStr(haystack, needle))