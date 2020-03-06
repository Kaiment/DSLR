import argparse
import srcs.helpers as helpers
import numpy as np
import matplotlib.pyplot as plt

class logisticRegression:
    def __init__(self, dataset): # should take two courses
        self.dataset = dataset
        self.houses = ["Slytherin", "Ravenclaw", "Gryffindor", "Hufflepuff"]
        self.results = np.array([])

    def read(self):
        data = helpers.dataToList(self.dataset)
        self.headers = data.pop(0)

        self.X_0 = self.headers.index("Herbology");
        self.X_1 = self.headers.index("Defense Against the Dark Arts")

        rows = []

        for key, row in enumerate(data):
            try:
                int(row[0])
                float(row[self.X_0])
                float(row[self.X_1])
                rows.append(row)
            except:
                pass

        data = rows;
        self.data = data;

        return self

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, theta, x):
        return self.sigmoid(np.dot(x, theta))

    def cost(self, theta, x, y):
        m = len(x)
        total = -(1 / m) * np.sum(y * np.log(self.predict(theta, x)) + (1 - y) * np.log(1 - self.predict(theta, x)))
        return total

    def compute_theta(self, theta, x, y):
        # compute the gradiant foreach x values
        m = x.shape[0]
        derivative = (1 / m) * np.dot(x.T, self.predict(theta, x) - y)

        return derivative

    def learn(self):
        # one vs all
        for house in self.houses:
            self.Ids = np.array([[int(row[0])] for row in self.data])
            self.Y = np.array([[1] if row[self.headers.index("Hogwarts House")] == house else [0] for row in self.data])
            self.X = np.array([[float(row[self.X_0]), float(row[self.X_1])] for row in self.data])
            self.theta = np.zeros((self.X.shape[1], 1))
            self.train()
            self.process_results()
        return self

    def train(self):
        learningRate = 0.0001
        epoch = 50000
        for key, e in enumerate(range(epoch)):
            if (key % 100 == 0):
                cost = self.cost(self.theta, self.X, self.Y)
                print("cost: "+str(cost))
            self.theta -= learningRate * self.compute_theta(self.theta, self.X, self.Y)
        return self

    def process_results(self):
        predicted = self.predict(self.theta, self.X)

        if len(self.results) > 0:
            self.results = np.append(self.results, predicted, axis = 1)
        else:
            self.results = predicted

    def get_predicted_house(self, rates):
        return self.houses[rates.argmax()]

    def compute_accuracy(self):
        correct = 0
        total = self.X.shape[0]

        for key, val in enumerate(self.data):
            if self.get_predicted_house(self.results[key]) == val[1]:
                correct += 1

        print("")
        print("Correctly predicted: " + str(correct) + " / " + str(total))
        print("Precision: " + str((100 * correct) / total) + " %")
        return self

    def write_rates(self):
        res = np.concatenate((self.Ids, self.results), axis=1)

        np.savetxt("weights.csv", res, delimiter=",", fmt="%f")    
        print("successfully saved weights in weights.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help="The training datatset")

    args = parser.parse_args()
    logisticObj = logisticRegression(args.dataset)
    logisticObj.read().learn().write_rates()
