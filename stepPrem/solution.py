memo = {}


def stepPerms(n):
    """
    given n number of stairs, determine the total number of ways to climb the
    stairs if you can take 1, 2, or 3 steps at a time
    """
    if n in memo:
        print(f"I have called mem the number is {n} = {memo[n]}")
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        f = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
    memo[n] = f
    return f


print(stepPerms(20))
