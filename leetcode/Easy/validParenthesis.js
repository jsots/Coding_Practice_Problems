let isValid = function(s) {
    let stack = []
    if (s.length % 2 !== 0) {
        return false
    }
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === "(" || s.charAt(i) === "{" || s.charAt(i) === "[") {
            stack.push(s.charAt(i))
        } else if (s.charAt(i) === ")") {
            if (stack[stack.length-1] === "(") {
                stack.pop()
            } else {
                return false
            }
        } else if (s.charAt(i) === "]") {
            if (stack[stack.length-1] === "[") {
                stack.pop()
            } else {
                return false
            }
        } else if (s.charAt(i) === "}") {
            if (stack[stack.length-1] === "{") {
                stack.pop()
            } else {
                return false
            }
        } else {
            return false
        }
    }
    if (stack.length !== 0) {
        return false
    }
    return true
};