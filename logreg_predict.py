import argparse
import numpy as np

class predict:
    def __init__(self, path):
        self.houses = ["Slytherin", "Ravenclaw", "Gryffindor", "Hufflepuff"]    
        self.weights_path = path

    def read(self):
        try:
            self.data = np.genfromtxt(self.weights_path, delimiter=",")
        except:
            exit("File not found")
        return self

    def compute(self):
        res = []
        for row in self.data:
            index = row[1:].argmax()
            res.append([int(row[0]), self.houses[index]])
        self.results = np.array(res)
        return self

    def write_houses(self):
        self.results = np.insert(self.results, 0, ["Index", "Hogwarts House"], axis=0)
        np.savetxt("houses.csv", self.results, fmt="%s", delimiter=",")
        print("successfully saved results in houses.csv")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("weights", help="The weights csv file")

    args = parser.parse_args()
    predictObj = predict(args.weights)
    predictObj.read().compute().write_houses()

if __name__ == "__main__":
    main()
