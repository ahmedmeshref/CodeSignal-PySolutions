"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""


def checkValidString(s):
    if len(s) == 0:
        return True
    nu_open = 0
    stack = []
    for p in s:
        if p == "(":
            nu_open += 1
            stack.append(p)
        elif p == "*":
            stack.append(p)
        else:
            if nu_open:
                ind = len(stack) - 1
                while stack[ind] != "(":
                    ind -= 1
                stack[ind], stack[-1] = stack[-1], stack[ind]
                stack.pop()
                nu_open -= 1
            elif stack:
                stack.pop()
            else:
                return False
    if nu_open and stack:
        nu_open = 0
        for char in stack:
            if char == "(":
                nu_open += 1
            elif nu_open:
                nu_open -= 1
        if nu_open > 0:
            return False
    return True

print(checkValidString("*())"))