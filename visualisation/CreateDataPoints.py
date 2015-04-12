__author__ = 'Milan'

import numpy as np

def makeDataPointsFromCluster(centroid, variance, amount):
    cov = [[variance[0], 0, 0],[0, variance[1], 0], [0, 0, variance[2]]]

    x, y, z = np.random.multivariate_normal(centroid, cov, amount).T

    return x, y, z


