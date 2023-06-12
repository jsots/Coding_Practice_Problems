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