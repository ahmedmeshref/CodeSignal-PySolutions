from collections import deque


def stringShift(s, shift_arr):
    dq = deque(s)
    for shift in shift_arr:
        if shift[0] == 1:
            for i in range(shift[1]):
                dq.appendleft(dq.pop())
        else:
            for i in range(shift[1]):
                dq.append(dq.popleft())
    return "".join(dq)


print(stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))
