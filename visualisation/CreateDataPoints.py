__author__ = 'Milan'

import numpy as np

def makeDataPointsFromCluster(cluster, amount):
    mean = cluster.getCentroid()
    variance = cluster.getVariance()
    cov = [[variance[0], 0, 0],[0, variance[1], 0], [0, 0, variance[2]]]

    x, y, z = np.random.multivariate_normal(mean, cov, amount).T

    return x, y, z


