import argparse
import srcs.helpers as helpers

class logisticRegression:
    def __init__(self, dataset):
        self.dataset = dataset

    def read(self):
        data = helpers.dataToList(self.dataset)
        self.headers = data.pop(0)

        self.data = data;
        
        self.Houses = [row[self.headers.index("Hogwarts House")] for row in data]
        self.X = [float(row[self.headers.index("Herbology")]) for row in data]
        self.Y = [float(row[self.headers.index("Defense Against the Dark Arts")]) for row in data]

        print(self.X[0])

        return self

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help="The training datatset")

    args = parser.parse_args()
    logisticObj = logisticRegression(args.dataset)
    logisticObj.read()
