from compute_metadata import *
from helpers import *
from matplotlib import pyplot

if __name__ == "__main__":
    data = dataToDict("../datasets/dataset_train.csv", 6)

    # pyplot.scatter(data["Arithmancy"], data["Astronomy"], marker='x', color="blue")
    
    i = 1
    visited = []

    for keyx, valx in data.items():
        for keyy, valy in data.items():
            if keyx != keyy and [keyx, keyy] not in visited and [keyy, keyx] not in visited:
                visited.append([keyx, keyy])
                pyplot.scatter(valx, valy, marker='x', color="purple")
                pyplot.xlabel(keyx)
                pyplot.ylabel(keyy)
                pyplot.subplot(6, 13, i)
                pyplot.tight_layout()
                i += 1

    print(len(visited))

    # pyplot.legend(colors.keys())
    pyplot.show()
