def missingNumber(nums):
    ourSum = 0
    for i in nums:
        if i % 2 == 0:
            ourSum -= i
        else:
            ourSum += i
    
    thisLen = len(nums) + 1
    ourResult = thisLen//2 if thisLen %2 == 0 else -1*(thisLen//2)
    
    return abs(ourSum - ourResult)
    