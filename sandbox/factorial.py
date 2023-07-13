def factorial(num):
    if num <= 1:
        return 1
    
    return num * factorial(num-1) 

# O(n) for time
# O(n) for space because of the call stack

def factorial_nonrecursive(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res


print(factorial(3))
print(factorial(4))
print(factorial(5))

print(factorial_nonrecursive(3))
print(factorial_nonrecursive(4))
print(factorial_nonrecursive(5))