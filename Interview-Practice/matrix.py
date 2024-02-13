# Given a message (string) and two constraints r (row) and c (column), create a cipher function that prints a message in the form of a matrix traveling from top to bottom, and then left to right (as opposed to going right to left, and then down the columns). 

# example: 

# string = "Hello"
# r = 3
# c = 2

# matrix =

# 'h' 'e' 'l'
# 'l' 'o' ' '  

# final string = 'hleol "


def stringMatrix(string, r, c):
    ans = []
    i = 0

    while i < len(string):
        row = []
        for j in range(i, i + r):
            if j<len(string):
                row.append(string[j].lower())
            else:
                break
            print(row)
        if len(row) == r:
            ans.append(row)
        else:
            for k in range(r - len(row)):
                row.append(" ")
            ans.append(row)
        i += r

    ans_array = []
    for y in range(len(ans[0])):
        for x in range(len(ans)):
            ans_array.append(ans[x][y])

    ans_string = "".join(ans_array)

    return ans_string
    


print(stringMatrix("Hello", 3, 2))
print(stringMatrix("tank", 3, 2))