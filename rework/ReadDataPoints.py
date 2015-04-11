__author__ = 'Milan'

import json

from BigDataProject.rework import DataPoint
import ClusterDB
import Cluster


file = open("dataset/yelp_academic_dataset_business.json")
clusterDb = ClusterDB()

def readAllDataPoints():
    while 1:
        lines = file.readlines(10000)   	# read the file by lines
        if not lines:
            break 							# break the loop when finishing reading the file
        for line in lines:
            data_json = json.loads(line)  	# convert the str to json format

            dataPoint = DataPoint(data_json["latitude"], data_json["longitude"],data_json["stars"] )

            checkDataPoint(dataPoint)

            checkAllClustersForCombining()

        printFoundClusters()

def checkDataPoint(dataPoint):
    for cluster in clusterDb.clusters:
        if cluster.checkDataPoint(dataPoint):
            cluster.addDataPoint(dataPoint)
            return

    newCluster = Cluster()
    newCluster.addDataPoint(dataPoint)
    clusterDb.addCluster(newCluster)

def checkAllClustersForCombining():
    for cluster in clusterDb.clusters:
        for otherCluster in clusterDb.clusters:
            if cluster == otherCluster:
                continue
            else:
                if cluster.checkCombineClusters(otherCluster):
                    cluster.combineClusters(otherCluster)
                    clusterDb.removeCluster(otherCluster)

def printFoundClusters():
    for cluster in clusterDb.clusters:
        print cluster.toString()