def computeStd(data, mean, count):
    std = 0
    for d in data:
        std += (d - mean)**2
     std /= count
     std = std**0.5
     return std
