__author__ = 'Milan'

import sys
import json

from BigDataProject.bfr.ClusterDB import ClusterDB
from BigDataProject.bfr.Cluster import Cluster

clusterDb = ClusterDB()

def readAllClusters():

    for line in sys.stdin:
        data_json = json.loads(line)  	# convert the str to json format

        cluster = Cluster()
        cluster.N = data_json["N"]
        cluster.SUM = data_json["SUM"]
        cluster.SUMSQ = data_json["SUMSQ"]

        clusterDb.addCluster(cluster)

        checkAllClustersForCombining()

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



readAllClusters()
printFoundClusters()


