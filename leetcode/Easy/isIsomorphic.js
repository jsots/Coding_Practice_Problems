var isIsomorphic = function(s, t) {
    if (s.length === t.length) {
        let sUnique = []
        let tUnique = []
        for (let i = 0; i < s.length; i++) {
            if (!sUnique.includes(s.charAt(i))) {
                sUnique.push(s.charAt(i))
            }
            if (!tUnique.includes(t.charAt(i))) {
                tUnique.push(t.charAt(i))
            }
        }
        if (sUnique.length === tUnique.length) {
            return true
        } else {
            return false
        }
    } else {
        return false
    }
};

// Solution discusses maps and sets. look into both of them

var isIsomorphic = function(s, t) {
    const map = new Map();
    const set = new Set();
    let n = s.length - 1;

    while (n >= 0) {
        if (map.has(s[n]) && map.get(s[n]) !== t[n]) {
        return false;
        }
        if (!map.has(s[n]) && set.has(t[n])) {
        return false;
        }
        set.add(t[n]);
        map.set(s[n], t[n]);
        n--;
    }

    return true;
};