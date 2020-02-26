# def jobOffers(scores, lowerLimits, upperLimits):
#     for l, u in zip(lowerLimits, upperLimits):
#        yield len([1 for score in scores if l <= score <= u])


def jobOffers(scores, lowerLimits, upperLimits):
    scores.sort()
    for l, u in zip(lowerLimits, upperLimits):
        k = 0
        r = len(scores)
        while (scores[k] < l) or (scores[r - 1] > u):
            if scores[k] < l:
                k += 1
            if scores[r - 1] > u:
                r -= 1
        return r - k


print(jobOffers([1, 2, 2, 2, 3], [1], [5]))
