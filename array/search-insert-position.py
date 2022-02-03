def searchInsert(nums, target):
    length = len(nums)
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return length
    key = length // 2
    left = 0
    right = length - 1
    while not (nums[key] == target or key == left):
        if nums[key] < target:
            left = key
        else:
            right = key

        key = (left + right) // 2

    return key if nums[key] == target else key + 1
    