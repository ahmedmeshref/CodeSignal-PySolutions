def subarraySum(nums, k):
    """
    Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
    """
    l = 0
    r = 0
    tot = 0
    while len(nums)-1 >= r >= l:
        if sum(nums[l: r + 1]) == k:
            tot += 1
            r += 1
        elif sum(nums[l: r + 1]) > k:
            l += 1
        else:
            r += 1
        if r == len(nums) - 1:
            l += 1
    return tot


nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))
