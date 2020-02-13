from compute_metadata import *
from helpers import *
import matplotlib

if __name__ == "__main__":
    data = dataToDict("../datasets/dataset_train.csv", 6)

    metaDataDict = getMetadata(data, data.keys())
    print(metaDataDict)
