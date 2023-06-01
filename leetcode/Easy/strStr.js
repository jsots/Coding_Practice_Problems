var strStr = function(haystack, needle) {
    if (haystack.includes(needle)) {
        let ans = haystack.split(needle)
        for(let i= 0; i<ans.length; i++) {
            if (ans[i] === needle) {
                return i
            }
        }
    }
    return ans
};

console.log(strStr)