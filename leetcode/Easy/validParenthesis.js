// Best solution for space O(n)

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

// Below is the most optimal solution in terms of time and space. Specifically time.

let isValid2 = function(s) {
    let stack = []
    if (s.length % 2 !== 0) {
        return false
    }
    for (let i = 0; i < s.length; i++) {
        let current = s.charAt(i)
        if (current === "(" || current === "{" || current === "[") {
            stack.push(current)
        } else if (current === ")") {
            if (stack[stack.length-1] === "(") {
                stack.pop()
            } else {
                return false
            }
        } else if (current === "]") {
            if (stack[stack.length-1] === "[") {
                stack.pop()
            } else {
                return false
            }
        } else if (current === "}") {
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