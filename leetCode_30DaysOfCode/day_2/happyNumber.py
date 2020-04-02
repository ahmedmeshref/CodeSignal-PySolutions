memo = {}


def isHappy(n):
    """
    Is happy takes in a number and returns True if it is a happy number, False otherwise. A happy number
    is a number defined by the following process: Starting with any positive integer, replace the number by the
    sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1.
    """
    try:
        if n == 1:
            return True
        if n in memo:
            return memo[n]
        memo[n] = 0
        k = 0
        while n:
            k += (n % 10) ** 2
            n = n // 10
        memo[n] = k
        return isHappy(k)
    except RecursionError:
        return False


print(isHappy(19))
