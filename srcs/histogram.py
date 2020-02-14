from compute_metadata import *
from helpers import *
from matplotlib import pyplot

if __name__ == "__main__":
    data = dataToDict("../datasets/dataset_test.csv", 6)
    metaDataDict = getMetadata(data, data.keys())
    
    colors = {"Arithmancy": "#eb4034", "Astronomy": "b","Herbology": "#eba834","Defense Against the Dark Arts": "#b1eb34","Divination": "#34eb8f","Muggle Studies": "#34d8eb","Ancient Runes": "#345eeb","History of Magic": "#345eeb","Transfiguration": "#eb34d3","Potions": "m","Care of Magical Creatures": "c","Charms": "g","Flying": "r"}

    i = 1
    for key, values in data.items():
        pyplot.subplot(4, len(data.keys()) / 4 + 1, i)
        i += 1
        pyplot.hist(values, 25, color=colors[key], density=True, alpha=0.4)
        pyplot.title(key+" => mean: "+str(round(metaDataDict[key]["mean"], 2))+", std: "+str(round(metaDataDict[key]["std"], 3)))
    pyplot.show()
