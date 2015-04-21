__author__ = 'ranveer'

import sys
import urllib2
import urllib
import json

try:
    url = "http://localhost:9200/drdoindex/drdo/_bulk"

    # Load File
    print "Loading File......"
    with open('data.txt') as raw_file:
        raw = raw_file.read()

    # Create Request
    print "Creating Request....."
    request = urllib2.Request(url, raw)

    # POST Data
    print "Posting Data to Elastic Cluster......"
    result = urllib2.urlopen(request)

    # Load Result
    print "Parsing Response from Elastic Server......"
    parsedresult = json.loads(result.read())

    # Print Server Response
    print "Printing Response from Elastic Server......"
    print parsedresult
	
except:
    print "Unexpected Error: ", sys.exc_info()