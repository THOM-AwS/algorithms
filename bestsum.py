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
            return remainderResult + [num]
        if shortest == None or len(remainderResult) < len(shortest):
            shortest = remainderResult + [num]
    
    return shortest