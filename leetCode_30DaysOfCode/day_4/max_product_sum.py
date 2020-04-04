def maxProduct(nums):
    s = 1
    negative = 1
    for num in nums:
        if num < 0:
            negative += 1
        s *= num
    if negative % 2 == 0:
        return s

    else:
        max_so_far = nums[0]
        curr_max = max_so_far
        for i in range(1, len(nums)):
            curr_max *= nums[i]
            if curr_max < nums[i]:
                curr_max = nums[i]
            if curr_max > max_so_far:
                max_so_far = curr_max
        return max_so_far


print(maxProduct([0, 2]))
