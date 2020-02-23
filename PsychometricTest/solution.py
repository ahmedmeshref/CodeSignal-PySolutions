# def jobOffers(scores, lowerLimits, upperLimits):
#     for l, u in zip(lowerLimits, upperLimits):
#        yield len([1 for score in scores if l <= score <= u])

def jobOffers(scores, lowerLimits, upperLimits):
    for l, u in zip(lowerLimits, upperLimits):
        return sum([2 if (l <= scores[i] <= u and l <= scores[i+ 1] <= u) else 1 if l <= scores[i] <= u or l <= scores[i+ 1] <= u else 0 for i in range(0, len(scores), 2)])


print(jobOffers([1, 2, 2, 2, 3], [2], [5]))
