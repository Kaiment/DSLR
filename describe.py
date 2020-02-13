from numpy import genfromtxt
from srcs.compute_metadata import *
import pprint

def dataToDict():
    data = genfromtxt("datasets/dataset_test.csv", delimiter=",", dtype=None, encoding="utf-8")
    header = data[0][6:]
    dataDict = {}
    for h in header:
        dataDict[h] = []
    for row in data[1:]:
        for j, col in enumerate(row[6:]):
            try:
                dataDict[header[j]].append(float(col))
            except:
                dataDict[header[j]].append(0.0)
    return [header, dataDict]

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

def main():
    header, data = dataToDict()
    metaDataDict = getMetadata(data, header)
    pprint.pprint(metaDataDict)
    #print(header)
    # print(data[0])
    # print(data[1])
    # print(data[2])
    # for e in data:
    #     print(e)

if __name__ == "__main__":
    main()
