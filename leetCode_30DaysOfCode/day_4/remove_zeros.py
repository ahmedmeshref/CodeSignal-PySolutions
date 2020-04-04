def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    counter = 0
    for i in range(len(nums) - 1):
        if nums[counter] == 0:
            nums.pop(counter)
            nums.append(0)
        else:
            counter += 1
    return nums


print(moveZeroes([0, 0, 1]))