from compute_metadata import *
from helpers import *
from matplotlib import pyplot

if __name__ == "__main__":
    data = dataToDict("../datasets/dataset_test.csv", 6)
    colors = {"Arithmancy": "#eb4034", "Astronomy": "b","Herbology": "#eba834","Defense Against the Dark Arts": "#b1eb34","Divination": "#34eb8f","Muggle Studies": "#34d8eb","Ancient Runes": "#345eeb","History of Magic": "#345eeb","Transfiguration": "#eb34d3","Potions": "m","Care of Magical Creatures": "c","Charms": "g","Flying": "r"}

    for key, val in data.items():
        pyplot.scatter(range(0, len(val)), val, marker='x', color=colors[key])
    pyplot.legend(colors.keys())
    pyplot.show()
