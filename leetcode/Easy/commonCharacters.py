def commonCharacters(strings):
    # Write your code here.
    common = {}
    ans = []
    added = False
    for word in strings:
        word_as_set = set(word)
        # Turning the word into a set allows us to only look at the unique charactes. 
        for char in word_as_set:
            if char in common:
                common[char] += 1
                if common[char] == len(strings):
                    ans.append(char)
            else:
                common[char] = 1
                if common[char] == len(strings):
                    ans.append(char)
            
            
    return ans
