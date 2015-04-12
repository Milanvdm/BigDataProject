__author__ = 'Milan'

import CreateDataPoints as cd
import json
import csv

id = 0

xThreshold = 0.1
yThreshold = 0.1

csvFile = open('ratings.csv', 'w')
writer = csv.writer(csvFile, delimiter=',')
titels = ['Id', 'Rating']
writer.writerows(titels)

jsonFile = open('points.json', 'w')

def createData():
    centroid = [0, 0, 0]
    variance = [0, 0, 0]
    x, y, z = cd.makeDataPointsFromCluster(centroid, variance, 100)

    startId = id

    json = createJson(x, y)
    createCsv(z, startId)

    json.dump(json, jsonFile)

def createCsv(z, startId):

    i = 0
    while i < z.size[0]:
        data = [startId, z[i]]
        writer.writerows(data)

        startId += 1
        i += 1

def createJson(x, y):
    features = makeFeatures(x, y)

    finalJson = {"type":"FeatureCollection","features":features}

    return finalJson

def makeFeatures(x, y):
    features = []

    i = 0
    while i < x.size[0]:
        long = x[i]
        lat = y[i]

        feature = {"type":"Feature","id":id,"properties":{"name":"datapoint"},"geometry":{"type":"Polygon","coordinates":[makePolygon(long, lat)]}},

        features.append(feature)

        i += 1
        id += 1

    return features

def makePolygon(x, y):
    rectangle = []

    upperLeft = [x - xThreshold, y + yThreshold]
    upperRight = [x + xThreshold, y + yThreshold]
    downLeft = [x - xThreshold, y - yThreshold]
    downRight = [x + xThreshold, y - yThreshold]

    rectangle.append(upperLeft)
    rectangle.append(upperRight)
    rectangle.append(downLeft)
    rectangle.append(downRight)

    return rectangle