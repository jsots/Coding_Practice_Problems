from collections import defaultdict

# List of words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = defaultdict(int)

# Your code here
for word in words:
    word_counts[word] += 1

# Print the word frequencies
for word, count in word_counts.items():
    print(f"{word}: {count}")


from collections import defaultdict
fruits = [("apple", "red"), ("banana", "yellow"), ("cherry", "red"), ("kiwi", "green")]
fruit_groups = defaultdict(list)

# Your code here
for f, c in fruits:
    fruit_groups[c].append(f)

# Print the grouped fruits
for color, fruit_list in fruit_groups.items():
    print(f"Fruits with color {color}: {', '.join(fruit_list)}")


from collections import defaultdict

# List of transactions as (customer, amount) tuples
transactions = [("Alice", 100), ("Bob", 50), ("Alice", 75), ("Eve", 30)]
customer_spending = defaultdict(int)

# Your code here
for c, s in transactions:
    customer_spending[c] += s

# Print the total spending for each customer
for customer, total in customer_spending.items():
    print(f"{customer}: {total}")

from collections import defaultdict

# List of names
names = ["Alice", "Bob", "Charlie", "Eve", "David", "Daniel"]
name_index = defaultdict(list)

# Your code here
for name in names:
    name_index[name[0]].append(name)

# Print the indexed names
for letter, name_list in name_index.items():
    print(f"Names starting with '{letter}': {', '.join(name_list)}")