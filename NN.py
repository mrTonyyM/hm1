import numpy as np;
class Nnetwork (object):

    def __init__(self,sizes):
        self.N_Layer = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x, y in zip(sizes[1:],sizes[:-1])]

    def sigmoid(z):
        return 1/(1 + np.exp(-z))

    def feedforward(self, a):
        for b, w in zip(self.biases,self.weights):
            a = sigmoid(np.dot(w, a ) + b)

    def SGD(self, trainig_data, epochs, mini_batch_size, eta, test_data = None):
        if test_data:
            n_test = len(test_data)
        n = len(trainig_data)
        for j in xrange(epochs):
            random.stuffle(trainig_data)
            mini_batches = [
                trainig_data[k:k+mini_batch_size]
                for k in xrange(0, n, mini_batch_size)]
            for mini_batchesself.update_mini_batches]