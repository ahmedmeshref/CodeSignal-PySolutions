from collections import Counter


def getLargestString(s, k):
    chars = Counter(s)
    keys = sorted(chars.keys(), reverse=True)
    new_s = ""
    for i in range(len(keys)):
        counter = i
        while chars.get(keys[i]):
            if new_s[-1] != keys[i]:
                new_s += keys[i] * k
            else:
                new_s += keys[counter] * k
    return new_s


print(getLargestString("yuzzvuyzpv", 1))
