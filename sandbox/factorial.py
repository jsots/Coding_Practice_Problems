def factorial(num):
    if num <= 1:
        return 1
    
    return num * factorial(num-1) 

# O(n) for time
# O(1) for space


print(factorial(3))
print(factorial(4))
print(factorial(5))