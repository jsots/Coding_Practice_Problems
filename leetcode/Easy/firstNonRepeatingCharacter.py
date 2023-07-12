def firstNonRepeatingCharacter(string):
    # Write your code here.
    unique_char = {}
    if string == "":
        return -1
    for i, char in enumerate(string):
        if char not in unique_char:
            unique_char[char] = i
        else:
            unique_char[char] = len(string)
        
        
    return min(unique_char.values()) if min(unique_char.values()) < len(string) else -1
