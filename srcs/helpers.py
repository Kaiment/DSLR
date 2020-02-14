from numpy import genfromtxt

def dataToDict(path, start_at):
    try:
        data = genfromtxt(path, delimiter=",", dtype=None, encoding="utf-8").tolist()
    except:
        exit("File not found, exiting...");
    header = data[0][start_at:]
    dataDict = {}
    for h in header:
        dataDict[h] = []
    for row in data[1:]:
        for j, col in enumerate(row[start_at:]):
            try:
                dataDict[header[j]].append(float(col))
            except:
                dataDict[header[j]].append(0.0)
    return dataDict

def dataToList(path):
    return genfromtxt(path, delimiter=",", dtype=None, encoding="utf-8").tolist()

def computeStd(data, mean, count):
    std = 0
    for d in data:
        std += (d - mean)**2
    std /= count
    std = std**0.5
    return std
