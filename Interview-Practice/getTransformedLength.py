def getTransformedLength(word, t):
    number_of_transformations = 0
    while number_of_transformations < t:
        transformed = ""
        for char in word:
            if char == "z":
                transformed += "ab"
            else:
                transformed += chr(ord(char) + 1)
        number_of_transformations += 1
        word = transformed
    return len(transformed)

print(getTransformedLength("defczx", 3))