# We have created a robot cat named Doraemon.
# Your job is to program him to move through a room.
# The room is represented by a 2D grid of one-byte characters.
# Doraemon is always facing up, down, left, or right.
# Doraemon can move one cell at a time (up, down, left, or right).
# When he moves to a new cell, he can read the one-byte character the cell contains.

# 1. Doraemon starts at the upper-left corner of the room, facing to the right.
# 2. If he is standing on a cat bed (@), return the location of the bed and stop.
# 3. If he is standing on an arrow (^ v < >), rotate him to face that direction.
# 4. Move him to the next space in the direction he is facing.
# 5. Goto 2

# You can return the coordinates using any data structure you like, as long as it is not ambiguous.

# Now teach Doraemon how to do arithmetic.
# As part of the solution, give him a stack of integers to work with.
# Additional rules:
# 0 .. 9 (digit) Push the integer value of this numeral on the stack. (e.g., 1 for ‘1’, etc.)
# - (subtract) Subtract the top two values on the stack and push the difference. Order matters: pop a; pop b; push b - a.
# When the program terminates, also return the value on the top of the stack, if there is one. Again, data structures are up to you.

# The program should still work with the previous rooms.

# Now program Doraemon with these additional rules:

# * (multiply) pop two values, a and b; push b * a
# $ (pop) pop the top of the stack and discard it
# : (duplicate) duplicate top of the stack
# S (swap) swap the two values on the top of the stack
# ? (conditional) Pop stack; if 0, set direction to right, else left



room = [
    ['v', ' ', ' ', ' '],
    [' ', ' ', '@', '<'],
    ['>', ' ', ' ', '^']
]   # Row 1, Column 2.

room_two = [
    ['v', ' ', ' ', ' '],
    [' ', ' ', '@', '<'],
    [' ', ' ', ' ', '^']
]

room_three = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', '@', '<'],
    [' ', ' ', ' ', '^']
]

room_four = [
    ['v', '@', '-', '-', '<'],
    ['>', '5', '4', '1', '^']
] # Row 0, Column 1, Value: 2

room_five = [
    ['v', '@', '-', '-', '<'],
    ['>', '5', '4', ' ', '^']
] 

room_six = [
    ['0','9',' ','>',':','1','-',':','v',' ',' ',' ',' ',' ','v',' ','*','?',' ',' ',' ','v'],
    [' ',' ',' ','^',' ',' ',' ',' ','?',' ',' ',' ','$',' ','v',' ',' ',' ',' ',' ',' ','$'],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','>','S',':','^',' ',' ',' ','@']
] # computes 9 factorial :)

# directions_to_moves = {
#     '>': [0, 1],
#     '<': [0, -1],
#     '^': [1, 0],
#     'v': [-1, 0],
# }

# ev solution: https://app.coderpad.io/NTR4MFZT

def catMoves(room):
    x = 0
    y = 0
    direction = "r"
    currentLocation = room[y][x]
    catStack = []
    a = 0
    b = 0
    while currentLocation != "@":
        print("x", x)
        print("y", y)
        print("direction", direction)
        print("currentLocation", currentLocation)

        if currentLocation == "v":
            direction = "d"
        if currentLocation == "^":
            direction = "u"
        if currentLocation == ">":
            direction = "r"
        if currentLocation == "<":
            direction = "l"
        if direction == "d":
            if y != len(room)-1:
                y += 1
            else:
                return "Sad Doraemon"
        if direction == "u":
            if y != 0:
                y -= 1
            else:
                return "Sad Doraemon"
        if direction == "r":
            if x != len(room[y])-1:
                x += 1
            else:
                return "Sad Doraemon"
        if direction == "l":
            if x != 0:
                x -= 1
            else:
                return "Sad Doraemon"
        if currentLocation == " ":
            direction = direction
        if currentLocation.isnumeric():
            catStack.append(int(currentLocation))
        if currentLocation == "-" and len(catStack) > 1:
            a = catStack.pop(-1)
            b = catStack.pop(-1)
            catStack.append(b-a)
        elif currentLocation == "-" and len(catStack) <= 1: 
            return "Doraemon looks confused"
        currentLocation = room[y][x]
    if len(catStack) != 0:
        print(f"Row {y}, Column {x}, CatStack: {catStack[-1]}")
    else:
        print(f"Row {y}, Column {x}, CatStack: {None}")
    return [y,x, catStack[-1] if len(catStack) != 0 else None]

# val_1 if cond else val_2

print(catMoves(room_five))




























def is_palindrome(phrase):
    # first, lowercase everything and strip anything not alpha
    letters = [letter for letter in phrase.lower() if letter.isalpha()]
    return letters == list(reversed(letters))

# print(is_palindrome('racecar'))
# print(is_palindrome('A man, a plan, a canal: Panama.'))
# print(is_palindrome(' '))
# print(is_palindrome('a racecar'))

# character = 'a'
# print(character.isalpha())

# phrase = 'racecar on a track'
# print([letter for letter in phrase if letter in ['a', 'b', 'c']]) # list comprehension

# # letters = []
# for letter in word:
#     letters.append(letter)

# print(letters)