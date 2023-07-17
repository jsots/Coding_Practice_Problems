def generateDocument(characters, document):
    # Write your code here.
    # Make two hash maps
    # See if they are equal, return True if yes
    # What do i do about spaces? Do these need to be considered?
    # Do capital letters matter?

    chars = {}

    for char in characters:
        chars[char] = 1 + chars.get(char, 0)
    for char in document:
        if char not in chars or chars[char] == 0:
            return False
        chars[char] = chars[char] - 1
        
    return True
