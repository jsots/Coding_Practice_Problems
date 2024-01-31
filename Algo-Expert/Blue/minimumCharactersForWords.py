def minimumCharactersForWords(words):
    # Write your code here.
    # iterate through the array
    # iterate through the letters in the string
    # store them, probably in a hashmap
    # i want to compare individual key totals, and replace with the highest
    # produce the values in the set as an array

    # do charactersw appear twice?
    # do i include punctiuation marks?
    # capital letters? 
    
    master_char = {}
    ans = []
    
    for word in words:
        current_char = {}
        for char in word:
            current_char[char] = current_char.get(char, 0) + 1 # consulted chat
        for key, value in current_char.items():
            master_char[key] = max(master_char.get(key, 0), value)

    ans = [] 
    # consulted chat
    for key, value in master_char.items():
        ans.extend([key] * value)

    return ans
