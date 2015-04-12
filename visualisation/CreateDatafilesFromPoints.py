__author__ = 'Milan'

import CreateDataPoints as cd
import json
import csv

class CreateData:

    def __init__(self):
        self.id = 0

        self.xThreshold = 1
        self.yThreshold = 1

        self.csvFile = open('ratings.csv', 'wb')
        self.writer = csv.writer(self.csvFile)
        titels = ["IdNumber", "Rating"]
        self.writer.writerow(titels)

        self.jsonFile = open('points.json', 'wb')

    def createData(self):
        centroid = [48, -102, 3]
        variance = [5, 5, 2]
        x, y, z = cd.makeDataPointsFromCluster(centroid, variance, 1000)

        startId = self.id

        jsonData = self.createJson(x, y)
        self.createCsv(z, startId)

        json.dump(jsonData, self.jsonFile)

    def createCsv(self, z, startId):

        i = 0
        while i < z.size:
            data = [startId, z[i]]
            self.writer.writerow(data)

            startId += 1
            i += 1

    def createJson(self, x, y):
        jsonData = {}
        jsonData["type"] = "FeatureCollection"
        jsonData["features"] = []

        self.makeFeatures(x, y, jsonData)


        return jsonData

    def makeFeatures(self, x, y, jsonData):
        i = 0
        while i < x.size:
            long = x[i]
            lat = y[i]

            feature = {}
            feature["geometry"] = {"type":"Polygon","coordinates":[self.makePolygon(long, lat)]}
            feature["properties"] = {"name":"datapoint"}
            feature["idNumber"] = self.id
            feature["type"] = "Feature"

            jsonData["features"].append(feature)

            i += 1
            self.id += 1

        return jsonData

    def makePolygon(self, x, y):
        rectangle = []

        upperLeft = [x - self.xThreshold, y + self.yThreshold]
        upperRight = [x + self.xThreshold, y + self.yThreshold]
        downLeft = [x - self.xThreshold, y - self.yThreshold]
        downRight = [x + self.xThreshold, y - self.yThreshold]

        rectangle.append(upperLeft)
        rectangle.append(upperRight)
        rectangle.append(downLeft)
        rectangle.append(downRight)

        return rectangle