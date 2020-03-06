from compute_metadata import *
from helpers import *
from matplotlib import pyplot

def main():
    data = dataToDict("../datasets/dataset_train.csv", 6)

    i = 0
    fig, sub = pyplot.subplots(13, 13)
    for keyX, valX in data.items():
        j = 0
        for keyY, valY in data.items():
            if i == 12:
                sub[i][j].set_xlabel(keyY)
            if j == 0:
                sub[i][j].set_ylabel(keyX)
            sub[i][j].scatter(valX, valY, marker='x', color="purple")    
            j += 1
        i += 1
    pyplot.show()

if __name__ == "__main__":
    main()
