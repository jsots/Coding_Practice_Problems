var lengthOfLastWord = function(s) {
    let ans = s.split(" ")
    for (let i=ans.length-1; i>=0; i--) {
        if (ans[i] !== "") {
            return ans[i].length
        }
    }
};