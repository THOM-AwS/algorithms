def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = bestSum(remainder, numbers)
        if remainderResult != None:
            combination = remainderResult + [num]
            if shortest == None or len(combination) < len(shortest):
                shortest = combination
    
    return shortest

print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25] # will take ages to run
print(bestSum(300, [7, 14])) # None # will never have the time to wait for this to finish
