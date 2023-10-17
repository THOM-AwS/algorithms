# python code for memoisation of Fibonacci series

def fib(n, memo={}):
    if (n in memo):
        return memo[n]
    elif (n <= 2):
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(50))
print(fib(100))
print(fib(1000))