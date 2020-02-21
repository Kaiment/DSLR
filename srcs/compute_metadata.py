from math import floor
from .helpers import *

def getMetadata(data, header):
    metaDataDict = {}
    for h in header:
        metaDataDict[h] = computeMetadata(data[h])
    return metaDataDict


def computeMetadata(data):
    count, mean, std, minValue, perc25, perc50, perc75, maxValue = computeBasics(data)
    return {
        "count": count,
        "mean": mean,
        "std": std,
        "min": minValue,
        "25": perc25,
        "50": perc50,
        "75": perc75,
        "max": maxValue
    }

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

def computePercentile(data, percentile, count):
    rank = percentile * (count -1) - 1
    rankInt = int(floor(rank))
    rankFraction = rank - rankInt
    return data[rankInt - 1] + rankFraction * (data[rankInt] - data[rankInt - 1])
