def foo(n):
    if(n <= 1):
        return 1
    foo(n - 1)

print(foo(10))
print(foo(100))
print(foo(500))