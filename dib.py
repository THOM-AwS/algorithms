def dib(n):
    if (n <= 1):
        return 1
    else:
        return n * dib(n - 1)
    
print(dib(10))
print(dib(100))