symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

let value = 0

let romanToInt = function(s) {
    value = 0;
    for(let i = 0; i < s.length; i+=1){
        let current = s[i]
        let next = s[i+1]
        symbols[current] < symbols[next] ? value -= symbols[current]: value += symbols[current]
    }
    return value
};

console.log(romanToInt("III"))
console.log(romanToInt("LVIII"))
console.log(romanToInt("MCMXCIV"))