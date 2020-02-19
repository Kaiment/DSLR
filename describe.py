from srcs.compute_metadata import *
from srcs.helpers import *
from srcs.describe_display import describeDisplay
import pprint

def main():
    data = dataToDict("datasets/dataset_test.csv", 6)
    header = data.keys()
    metaDataDict = getMetadata(data, header)
    describeDisplay(metaDataDict)

if __name__ == "__main__":
    main()
