from srcs.compute_metadata import *
from srcs.helpers import *
import pprint

def main():
    data = dataToDict("datasets/dataset_test.csv", 6)
    header = data.keys()
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
