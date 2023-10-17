def cansum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    for num in numbers:
        remainder = targetSum - num
        if cansum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(cansum(7, [2, 3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
print(cansum(300, [7, 14]))