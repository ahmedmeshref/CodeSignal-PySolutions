"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

"""


def removeDuplicates(nums):
    """
    TimeComplexity: O(n)
    SpaceComplexity: O(1)
    """
    counter = 0
    for i in range(len(nums) - 1):
        if nums[counter] == nums[counter + 1]:
            nums = nums[0:counter] + nums[counter+1:]
        else:
            counter += 1
    return nums


print(removeDuplicates([1, 1, 2]))
