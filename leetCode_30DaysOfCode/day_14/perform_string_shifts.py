from collections import deque


def stringShift(s, shift_arr):
    dq = deque(s)
    for shift in shift_arr:
        dq.rotate((2*shift[0] - 1) * shift[1])
    return "".join(dq)


print(stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))


