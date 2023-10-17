# python function to find the paths through a grid

def gridtraveller(n,m):
    if(n == 1 and m == 1):
        return 1
    elif(n == 0 or m == 0):
        return 0
    else:
        return gridtraveller(n-1,m) + gridtraveller(n,m-1)
    
print(gridtraveller(5,3))
print(gridtraveller(2,3))
print(gridtraveller(3,2))
print(gridtraveller(3,3))
print(gridtraveller(10,10)) 
print(gridtraveller(18,18)) # this will take a long time to run
print(gridtraveller(25,25))
print(gridtraveller(30,30))
print(gridtraveller(100,100))