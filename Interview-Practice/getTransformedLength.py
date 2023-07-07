def getTransformedLength(word, t):
    transformed = ""
    number_of_transformations = 0
    while number_of_transformations < t:
        for char in word:
            if char == z:
                transformed += "ab"
            else:
                transformed += chr(ord(char) + 1)
        number_of_transformations += 1
    return len(transformed)

print(getTransformedLength("defcz", 8))