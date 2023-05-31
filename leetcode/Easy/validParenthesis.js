let isValid = function(s) {
    let stack = []
    if (s.length % 2 !== 0) {
        return false
    }
    for (let i = 0; i < s.length; i++) {
        let current = s.charAt(i)
        let topOfStack = stack[stack.length-1]
        if (current === "(" || current === "{" || current === "[") {
            stack.push(current)
        } else if (current === ")") {
            if (topOfStack === "(") {
                stack.pop()
            } else {
                return false
            }
        } else if (current === "]") {
            if (topOfStack === "[") {
                stack.pop()
            } else {
                return false
            }
        } else if (current === "}") {
            if (topOfStack === "{") {
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