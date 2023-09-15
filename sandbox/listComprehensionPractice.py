# These are practice problems from chat gpt to work on list comprehensions:
from collections import defaultdict


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
ans_3 = [len(word) for word in test_3]
print(ans_3)

# Uppercase Conversion: Given a list of strings, create a new list that contains the uppercase versions of each string in the original list.

test_4 = ['hello', 'world', 'python']
# Output: ['HELLO', 'WORLD', 'PYTHON']
ans_4 = [word.upper() for word in test_4]
print(ans_4)

# Filter by Length: Given a list of words, create a new list that contains only the words with a length greater than a specified value.

test_5 = ['apple', 'banana', 'cherry', 'date'] 
length = 5
# Output: ['banana', 'cherry']
ans_5 = [word for word in test_5 if len(word) > length]
print(ans_5)

# Character Frequency: Given a string, create a dictionary where keys are characters and values are the frequencies of those characters in the string.

test_6 = 'programming'
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
ans_6 = {char: test_6.count(char) for char in test_6}
print(ans_6)

# Transpose Matrix: Given a matrix (list of lists), create a new matrix that is the transpose of the original matrix.

test_7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
ans_7 = [[row[i] for row in test_7] for i in range(len(test_7))]
print(ans_7)




# Word Length Frequency
# Given a list of words, create a dictionary where the keys are word lengths, and the values are the frequencies of words with those lengths in the list.

test_8 = ['apple', 'banana', 'cherry', 'date', 'fig']
# Output: {5: 1, 6: 2, 4: 1, 3: 1}
ans_8 = {len(word): test_8.count(word) for word in test_8}
print(ans_8)

# Vowel Count
# Given a string, create a dictionary where the keys are vowels (a, e, i, o, u) and the values are the frequencies of those vowels in the string.

test_9 = 'programming is fun'
# Output: {'a': 1, 'e': 0, 'i': 3, 'o': 1, 'u': 1}
vowels = {"a", "e", "i", "o", "u"}
vowel_count = defaultdict(int)
ans_9 = {char: test_9.count(char) for char in test_9 if char.lower() in vowels}
print(ans_9)

# Character Frequency without Count Method
# Given a string, create a dictionary where the keys are characters, and the values are the frequencies of those characters in the string. Solve this problem without using the count method.
# Example:
# Input: 'programming'
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# Matrix Diagonal
# Given a square matrix (list of lists), create a list containing the elements of the diagonal of the matrix.
# Example:
# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 5, 9]

# Flatten Matrix
# Given a matrix (list of lists), create a flattened list containing all the elements from the matrix.
# Example:
# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pairs from Two Lists
# Given two lists, create a list of tuples where each tuple contains one element from each list.
# Example:
# Input: [1, 2, 3] and ['a', 'b', 'c']
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# print("Hello")

# def number_of_points(nums):
#     intercept_set = set()

#     for num in nums:
#         step = num[0]
#         for i in range(num[0], num[1]+1):
#             intercept_set.add(step)
#             step += 1
#     return len(intercept_set)

# # if __name__ == "__main__":
# #   fptr = open(os.environ['OUTPUT_PATH'], "w")

# #   nums_rows = int(input().strip))
# #   nums_columns = int(input().strip())
  
# #   nums = []
  
# #   for _ in range(nums_rows):
# #     nums.append(list(map(int, input().rstrip().split())))
  
# #   result = number_of_points(nums)
  
# #   fptr.write(str(result) + "\n")
  
# #   # fptr.close()

# print(number_of_points([[3,6], [1,5], [4,7]]))
# print(number_of_points([[1,3], [5,8]]))
# print(number_of_points([[-1,3], [5,8]]))
# # print(number_of_points([[]]))
# print("Hello")


print("Ans below:")
def merge_intervals(intervals):
    ans = []
    i = 0

    while i < len(intervals):
        temp = []
        j = i + 1
        check_top = intervals[i][1]
        while j < len(intervals) and check_top >= intervals[j][0]:
            check_top = intervals[j][1]
            j += 1
        low = min(intervals[i][0], intervals[j-1][0])
        high = max(intervals[i][1], intervals[j-1][1])
        temp.append(low)
        temp.append(high)
        ans.append(temp)
        i = j

    return ans

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
print(merge_intervals([[1,4], [4,5]]))
print(merge_intervals([[1,3], [3,5], [4,5]]))
print(merge_intervals([[1,1], [2,5], [1,2]]))