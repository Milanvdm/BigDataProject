__author__ = 'Milan'

import folium
import pandas as pd

import CreateDatafilesFromPoints as cdfp

cdfp.createData()

allDatapoints = r'points.json'
ratings = r'ratings.csv'

ratings_data = pd.read_csv(ratings)

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
map.geo_json(geo_path=allDatapoints, data=ratings_data,
             columns=['Id', 'Rating'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Ratings [0-5]')
map.create_map(path='clusterMap.html')

