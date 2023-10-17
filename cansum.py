def cansum(targetSum, numbers):
    if (targetSum == 0):
        return True
    elif (targetSum < 0):
        return False
    for num in numbers:
        remainder = targetSum - num
        if (cansum(remainder, numbers)) == True:
            return True
    return False

print(cansum(7, [2, 3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
print(cansum(300, [7, 14]))
