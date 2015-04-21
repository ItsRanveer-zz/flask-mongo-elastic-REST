__author__ = 'ranveer'

import sys
import os
import json
import pymongo

try:
    # Load File
    print 'Opening JSON File......'
    with open('raw.json') as raw_file:
        raw = json.load(raw_file)

    singlejson = {}
    alljson = []
    # Iterate through the "data" and assign keys to the values in it from "fields"
    print 'Parsing Data for inserting........'
    for single in raw['data']:

        for i in range(len(raw['fields'])):

            singlejson[raw['fields'][i]['label']] = single[i]

        alljson.append(singlejson.copy())

	# Connect to mongo running on port : 27017
    print 'Connecting to MongoDB at 27017........'
    connection = pymongo.MongoClient(host="mongodb://localhost:27017")
    db = connection.gov
    drdo = db.drdo
	
    # Put data in mongoDB
    print 'Putting Data in MongoDB.........'
    drdo.insert(alljson)
    print 'Data Inserted SuccessFully..........'
	
except:
    print "Unexpected Error: ", sys.exc_info()