"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

def main(nums, target):
    if not nums:
        return -1
    l, r = two_sorted(nums)
    ind = binary_search(nums, 0, l, target)
    if ind == -1:
        ind = binary_search(nums, r + 1, len(nums) - 1, target)
        if ind == -1:
            return -1
    return ind

def two_sorted(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > arr[l]:
            l = mid
        else:
            r = mid
    return (l, r)


def binary_search(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1





print(main([7, 1, 2, 3, 4, 5, 6], 6))
