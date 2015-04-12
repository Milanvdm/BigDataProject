__author__ = 'Milan'

import folium
import CreateDataPoints as cd
import matplotlib.pyplot as plt
import matplotlib as mpl

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
cmap = plt.get_cmap("afmhot")
mixer = mpl.cm.ScalarMappable(mpl.colors.Normalize(vmin=0, vmax=5), cmap)

def makeMarkers():
    x, y, z = createData()

    i = 0
    while i < x.size:
        color = decideColor(z[i])
        map.polygon_marker(location=[x[i], y[i]],
                     fill_color=color, line_opacity=0, num_sides=4, radius=5, rotation=0)

        i += 1

def decideColor(ratingValue):
    hexcolor = mpl.colors.rgb2hex(mixer.to_rgba(ratingValue))
    print str(hexcolor)
    return str(hexcolor)

def createData():
        centroid = [48, -102, 3]
        variance = [1, 1, 2]
        x, y, z = cd.makeDataPointsFromCluster(centroid, variance, 1000)

        return x, y, z



makeMarkers()
map.create_map(path='clusterMap.html')

