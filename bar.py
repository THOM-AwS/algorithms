def bar(n):
    if (n <= 1):
        return 1
    bar(n - 2)
    
print(bar(10))
print(bar(100))
print(bar(500))
