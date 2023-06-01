var lengthOfLastWord = function(s) {
    let ans = s.split(" ")
    let lastIndex = ans.length-1
    for (let i=lastIndex; i>=0; i--) {
        if (ans[i] !== "") {
            return ans[i].length
        }
    }
};