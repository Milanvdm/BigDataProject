__author__ = 'Milan'

class ClusterDB:
    def __init__(self):
        self.clusters = []

    def addCluster(self, cluster):
        self.clusters.append(cluster)

    def removeCluster(self, cluster):
        self.clusters.remove(cluster)

