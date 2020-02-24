# def jobOffers(scores, lowerLimits, upperLimits):
#     for l, u in zip(lowerLimits, upperLimits):
#        yield len([1 for score in scores if l <= score <= u])

def jobOffers(scores, lowerLimits, upperLimits):
    for l, u in zip(lowerLimits, upperLimits):
        return len(list(filter(lambda x: l <= x <= u, scores)))


print(jobOffers([1, 2, 2, 2, 3], [2], [5]))
