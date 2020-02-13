from math import floor

def computeBasics(data):
    count = 0
    mean = 0
    minValue = float("inf")
    maxValue = float("-inf")
    for d in data:
        if d != '':
            count += 1
            mean += d
            if d < minValue:
                minValue = d
            elif d > maxValue:
                maxValue = d
    mean /= count
    std = computeStd(data, mean, count)
    data.sort()
    perc25 = computePercentile(data, 0.25, count)
    perc50 = computePercentile(data, 0.5, count)
    perc75 = computePercentile(data, 0.75, count)
    return [count, mean, std, minValue, perc25, perc50, perc75, maxValue]

def computeStd(data, mean, count):
    std = 0
    for d in data:
        std += (d - mean)**2
    std /= count
    std = std**0.5
    return std

def computePercentile(data, percentile, count):
    rank = percentile * (count -1) - 1
    rankInt = int(floor(rank))
    rankFraction = rank - rankInt
    return data[rankInt - 1] + rankFraction * (data[rankInt] - data[rankInt - 1])
