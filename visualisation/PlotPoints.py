__author__ = 'Milan and Rob'

import folium
import pandas as pd

#Median Household income
map_osm = folium.Map(location=[45.5236, -122.6750])
map_osm.create_map(path='osm.html')