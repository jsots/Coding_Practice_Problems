var wordPattern = function(pattern, s) {
    let patternLetters = pattern.split("")
    let sLetters = s.split(" ")
    let dictionary = {}
    if (patternLetters.length !== sLetters.length) {
        return false
    }
    for (let i = 0; i < patternLetters.length; i++) {
        if (dictionary[patternLetters[i]]) {
            if (dictionary[patternLetters[i]])
        }
    }
};

console.log(wordPattern("abba", "dog cat cat dog"))