def lib(n):
    if(n <= 1):
        return 1
    lib(n-2)
    lib(n-2)
    
print(lib(4))
print(lib(5))
print(lib(6))