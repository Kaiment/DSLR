from compute_metadata import *
from helpers import *
from matplotlib import pyplot

if __name__ == "__main__":
    data = dataToDict("../datasets/dataset_test.csv", 6)

    courseStds = {}

    metaDataDict = getMetadata(data, data.keys())
    for key, values in metaDataDict.items():
        courseStds[key] = 1 / values["std"]
    print(courseStds)
    pyplot.bar(courseStds.keys(), courseStds.values(), 0.3, color='g', align="edge")
    pyplot.subplots_adjust(bottom=0.5)
    pyplot.xticks(rotation=-90);
    pyplot.show()
