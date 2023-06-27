var wordPattern = function(pattern, s) {
    let patternLetters = pattern.split("")
    let sLetters = s.split(" ")
    let dictionary = {}
    if (patternLetters.length !== sLetters.length) {
        return false
    }
    for (let i = 0; i < patternLetters.length; i++) {
        if (dictionary[patternLetters[i]]) {
            if (!Object.values(dictionary).includes(sLetters[i])) {
                return false
            }
        } else {
            if (Object.values(dictionary).includes(sLetters[i])) {
                return false
            }
            dictionary[patternLetters[i]] = sLetters[i]
        }
    }
    return true
};

console.log(wordPattern("abba", "dog cat cat dog"))