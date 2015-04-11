__author__ = 'Milan'

import sys
import json

from BigDataProject.bfr.DataPoint import DataPoint
from BigDataProject.bfr.ClusterDB import ClusterDB
from BigDataProject.bfr.Cluster import Cluster

clusterDb = ClusterDB()

def readAllDataPoints():
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # convert the str to json format
        data_json = json.loads(line)
        dataPoint = DataPoint(data_json["latitude"], data_json["longitude"],data_json["stars"])
        # add the dict to the list
        checkDataPoint(dataPoint)

        checkAllClustersForCombining()


def readAllDataPoints():
    for line in file:
        data_json = json.loads(line)  	# convert the str to json format

        dataPoint = DataPoint(data_json["latitude"], data_json["longitude"],data_json["stars"])

        checkDataPoint(dataPoint)

        checkAllClustersForCombining()


def checkDataPoint(dataPoint):
    for cluster in clusterDb.clusters:
        if cluster.checkDataPoint(dataPoint):
            print 'Add point to: ' + cluster.toString()
            cluster.addDataPoint(dataPoint)
            print 'and gives: ' + cluster.toString()
            return

    newCluster = Cluster()
    newCluster.addDataPoint(dataPoint)
    clusterDb.addCluster(newCluster)
    print 'Made new cluser: ' + newCluster.toString()

def checkAllClustersForCombining():
    for cluster in clusterDb.clusters:
        for otherCluster in clusterDb.clusters:
            if cluster == otherCluster:
                continue
            else:
                if cluster.checkCombineClusters(otherCluster):
                    print 'Combined cluster: ' + cluster.toString() + ' and ' + otherCluster.toString()
                    cluster.combineClusters(otherCluster)
                    clusterDb.removeCluster(otherCluster)
                    print 'Combined cluster to: ' + cluster.toString()

def printFoundClusters():
    for cluster in clusterDb.clusters:
        print cluster.toString()



readAllDataPoints()
printFoundClusters()