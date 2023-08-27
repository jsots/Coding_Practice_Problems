# These are practice problems from chat gpt to work on list comprehensions:



# Squares of Numbers: Given a list of numbers, create a new list that contains the squares of each number in the original list.

test_1 = [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]
ans_1 = [num**2 for num in test_1]
print(ans_1)

# Even Numbers: Given a list of numbers, create a new list that contains only the even numbers from the original list.

test_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10]
ans_2 = [num for num in test_2 if num % 2 == 0]
print(ans_2)

# Words Length: Given a list of words, create a new list that contains the lengths of each word in the original list.

test_3 = ['apple', 'banana', 'cherry', 'date']
# Output: [5, 6, 6, 4]

# Uppercase Conversion: Given a list of strings, create a new list that contains the uppercase versions of each string in the original list.

test_4 = ['hello', 'world', 'python']
# Output: ['HELLO', 'WORLD', 'PYTHON']

# Filter by Length: Given a list of words, create a new list that contains only the words with a length greater than a specified value.

test_5 = ['apple', 'banana', 'cherry', 'date'] 
length = 5
# Output: ['banana', 'cherry']

# Character Frequency: Given a string, create a dictionary where keys are characters and values are the frequencies of those characters in the string.

test_6 = 'programming'
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# Transpose Matrix: Given a matrix (list of lists), create a new matrix that is the transpose of the original matrix.

test_7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]