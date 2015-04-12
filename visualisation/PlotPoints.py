__author__ = 'Milan'

import folium
import pandas as pd

from CreateDatafilesFromPoints import CreateData

createData = CreateData()
createData.createData()
createData.csvFile.close()

allDatapoints = r'points.json'
ratings = r'ratings.csv'

ratings_data = pd.read_csv(ratings, skip_blank_lines=True)

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
map.geo_json(geo_path=allDatapoints, data=ratings_data,
             columns=['IdNumber', 'Rating'],
             key_on='feature.idNumber',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Ratings')
map.create_map(path='clusterMap.html')

