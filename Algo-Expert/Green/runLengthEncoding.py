def runLengthEncoding(string):
    # Write your code here.
    # Think about the order of the lettes
    # Think about why 9 is the max. in an interview they might not tell you that

    chars = []
    length = 1
    
    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i - 1]
        if prev != curr or length == 9:
            chars.append(str(length))
            chars.append(prev)
            length = 0
       
        length += 1

    chars.append(str(length))
    chars.append(string[len(string) - 1])
    return "".join(chars)