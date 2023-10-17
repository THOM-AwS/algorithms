# python function to find the paths through a grid with memoisation


def gridtraveller(n,m, memo={}):
    key = str(m) + ',' + str(n)
    if(key in memo):
        return memo[key]
    
    if(n == 1 and m == 1):
        return 1
    elif(n == 0 or m == 0):
        return 0
    else:
        memo[key] = gridtraveller(n-1,m, memo) + gridtraveller(n,m-1, memo)
        return memo[key]

print(gridtraveller(5,3))
print(gridtraveller(2,3))
print(gridtraveller(3,2))
print(gridtraveller(3,3))
print(gridtraveller(10,10))
print(gridtraveller(18,18))
print(gridtraveller(25,25))
print(gridtraveller(30,30))
print(gridtraveller(100,100))
print(gridtraveller(500,500))