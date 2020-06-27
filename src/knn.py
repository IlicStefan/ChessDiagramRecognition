################################################################################
# K nearest neighbor classifier
################################################################################

import numpy as np


class KNearestNeighbor(object):
    def __init(self):
        pass

    def train(self, X, y):
        self.Xtr = X
        self.ytr = y

    def predict(self, X, distance="L1", k=1):
        num_test = X.shape[0]
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)

        for i in range(num_test):
            if distance == "L2":
                distances = np.sum((self.Xtr - X[i, :]) ** 2, axis=1)
            else:
                distances = np.sum(np.abs(self.Xtr - X[i, :]), axis=1)
            k_index = np.argpartition(distances, k)[:k]
            counts = np.bincount(self.ytr[k_index])
            index = np.argmax(counts)
            Ypred[i] = index

        return Ypred
