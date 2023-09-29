# 1. Create a list comprehension that generates a list of all even numbers from 1 to 20.

list_1 = [num for num in range(1, 20) if num % 2 == 0]
print(list_1)

# 2. Write a list comprehension that computes the square of each number in a given list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [num ** 2 for num in numbers]
print(list_2)

# 3. Given a string, create a list comprehension that extracts all the vowels (lowercase) from the string.
input_string = "Hello, World!"
vowels = {"a", "e", "i", "o", "u"}
list_3 = [char for char in input_string if char in vowels]
print(list_3)

# 4. Generate a list of positive numbers from a given list of integers.
integers = [-2, 5, -8, 10, -3, 7, 0]
list_4 = [num for num in integers if num >= 0]
print(list_4)

# 5. Given a list of words, create a list comprehension that returns only the words with a length greater than 5 characters.
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# 6. Generate a list of the squares of all odd numbers from 1 to 30.

# 7. Write a list comprehension that generates a list of prime numbers from 1 to 50.

# 8. Create a list comprehension that extracts all uppercase letters from a given string.
input_string = "Hello, World!"

# 9. Generate a list of numbers from 1 to 100 that are divisible by both 3 and 5.

# 10. Given a list with duplicate elements, create a list comprehension to remove duplicates and return a list with only unique elements.
duplicate_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
