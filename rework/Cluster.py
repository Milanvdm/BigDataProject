__author__ = 'Milan'

import numpy as numpy

class Cluster:
        referenceVariance = [0, 0, 0]
        distanceThreshold = 20
        deviationMult = 2

        def __init__(self):
            self.N = 0
            self.SUM = [0, 0, 0]
            self.SUMSQ = [0, 0, 0]

        def getCentroid(self):
            centroid = []

            centroid.append(self.SUM[0]/self.N)
            centroid.append(self.SUM[1]/self.N)
            centroid.append(self.SUM[2]/self.N)

            return centroid

        def getVariance(self):
            variance = self.calculateVariance(self.N, self.SUM, self.SUMSQ)

            return variance

        def getStandardDeviation(self):
            variance = self.getVariance()

            normVariance = numpy.linalg.norm(variance)
            deviation = normVariance**0.5

            return deviation

        def calculateVariance(self, N, SUM, SUMSQ):
            variance = []

            variance.append(float(self.SUMSQ[0])/self.N - (float(self.SUM[0])/self.N)**2)
            variance.append(float(self.SUMSQ[1])/self.N - (float(self.SUM[1])/self.N)**2)
            variance.append(float(self.SUMSQ[2])/self.N - (float(self.SUM[2])/self.N)**2)

            return variance

        def addDataPoint(self, dataPoint):
            self.N += 1

            self.SUM[0] += dataPoint.lat
            self.SUM[1] += dataPoint.long
            self.SUM[2] += dataPoint.rating

            self.SUMSQ[0] += dataPoint.lat**2
            self.SUMSQ[1] += dataPoint.long**2
            self.SUMSQ[2] += dataPoint.rating**2

        def calculateMd(self, dataPoint):
            md = [0, 0, 0]
            centroid = self.getCentroid()
            variance = self.getVariance()

            md[0] = ((dataPoint.lat - centroid[0])/variance[0])**2
            md[1] = ((dataPoint.long - centroid[1])/variance[1])**2
            md[2] = ((dataPoint.rating - centroid[2])/variance[2])**2

            return (md[0] + md[1] + md[2])**0.5

        def checkDataPoint(self, dataPoint):
            if self.N == 1:
                if self.checkDataPointSpecial(dataPoint):
                    self.addDataPoint(dataPoint)

            else:
                md = self.calculateMd(dataPoint)

                if md < self.deviationMult * self.getStandardDeviation():
                    self.addDataPoint(dataPoint)

        def checkDataPointSpecial(self, dataPoint):
            newCluster = Cluster()
            newCluster.addDataPoint(dataPoint)
            if self.checkCombineClusters(newCluster):
                return True
            else:
                return False

        def checkCombineClusters(self, otherCluster):
            joinedN = self.N + otherCluster.N
            joinedSUM = self.SUM + otherCluster.SUM
            joinedSUMSQ = self.SUMSQ + otherCluster.SUMSQ

            variance = self.calculateVariance(joinedN, joinedSUM, joinedSUMSQ)

            if self.belowVarianceThreshold(variance):
                return True
            else:
                return False


        def belowVarianceThreshold(self, combinedVariance):
            distance = numpy.linalg.norm(combinedVariance - self.referenceVariance)

            if distance < self.distanceThreshold:
                return True
            else:
                return False


        def combineClusters(self, otherCluster):
            self.N += 1

            self.SUM[0] += otherCluster.SUM[0]
            self.SUM[1] += otherCluster.SUM[1]
            self.SUM[2] += otherCluster.SUM[2]

            self.SUMSQ[0] += otherCluster.SUMSQ[0]
            self.SUMSQ[1] += otherCluster.SUMSQ[1]
            self.SUMSQ[2] += otherCluster.SUMSQ[2]

        def toString(self):
            toString = "[" + str(self.N) + ", " + str(self.SUM) + ", " + str(self.SUMSQ) + "]"

            return toString