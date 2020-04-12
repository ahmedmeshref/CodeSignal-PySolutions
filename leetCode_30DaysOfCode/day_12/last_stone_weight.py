"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""


def lastStoneWeight(stones):
    def getLast(arr):
        ind = arr.index(max(arr))
        arr[-1], arr[ind] = arr[ind], arr[-1]
        return arr.pop()

    while len(stones) > 1:
        # delete the largest ele from the stones list
        largest = getLast(stones)
        sec_largest = getLast(stones)
        if largest > sec_largest:
            stones.append(largest - sec_largest)
    if stones:
        return stones[0]
    return 0


print(lastStoneWeight([5,3,2,10]))