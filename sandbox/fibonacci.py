def fibonnaci(num):
    if num <= 1:
        return num

    return fibonnaci(num-1) + fibonnaci(num-2)

print(fibonnaci(1))
print(fibonnaci(2))
print(fibonnaci(3))
print(fibonnaci(4))
print(fibonnaci(6))
print(fibonnaci(10))