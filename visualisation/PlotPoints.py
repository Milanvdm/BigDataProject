__author__ = 'Milan'

import folium
import CreateDataPoints as cd
import matplotlib.pyplot as plt
import matplotlib as mpl

import ast

from BigDataProject.bfr.Cluster import Cluster

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
cmap = plt.get_cmap("afmhot")
mixer = mpl.cm.ScalarMappable(mpl.colors.Normalize(vmin=0, vmax=5), cmap)

def makeMarkers(x, y, z):

    i = 0
    while i < len(x):
        color = decideColor(z[i])
        map.polygon_marker(location=[x[i], y[i]],
                     fill_color=color, line_opacity=0, num_sides=4, radius=5, rotation=0)

        i += 1

def decideColor(ratingValue):
    hexcolor = mpl.colors.rgb2hex(mixer.to_rgba(ratingValue))
    return str(hexcolor)

def createMap():
        clusters = readClusters()

        for cluster in clusters:
            centroid = cluster.getCentroid()
            centroid[2] = centroid[2]/10
            variance = cluster.getVariance()
            variance[2] = variance[2]/10
            amount = cluster.N

            x, y, z = cd.makeDataPointsFromCluster(centroid, variance, 10)

            makeMarkers(x, y, z)

def readClusters():
    clusters = []

    with open("clusters.txt", "r") as input:
        for line in input:
            lst = ast.literal_eval(line)

            newCluster = Cluster()
            newCluster.N = lst[0]
            newCluster.SUM = lst[1]
            newCluster.SUMSQ = lst[2]

            clusters.append(newCluster)

    return clusters

createMap()
map.create_map(path='clusterMap.html')

