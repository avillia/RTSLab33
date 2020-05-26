import numpy as np


class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=4, learning_rate=0.1):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


if __name__ == '__main__':

    # Basic setups
    A = [0, 6]
    B = [1, 5]
    C = [3, 3]
    D = [2, 4]

    speeds = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3]

    time_deadline = [0.5, 1, 2, 5]

    iter_deadline = [100, 200, 500, 1000]

    threshold = 4

    # Adjusting training inputs

    training_inputs = [np.array(A), np.array(B), np.array(C), np.array(D)]

    label = np.array([1, 0, 0, 0])

    # Training

    perceptron = Perceptron(2, learning_rate=speeds[4])
    perceptron.train(training_inputs, label)

    # Results printing

    print(perceptron.predict(np.array([3, 4])))
    print(perceptron.predict(np.array([0, 7])))
