__author__ = 'ranveer'

import json
import urllib2
import urllib

class SearchElastic:

    # Constructor for the class
    def __init__(self, host):
        self.hosturl = host

    def search(self, searchType, searchText):
        result = ""
        url = self.hosturl + "/drdoindex/drdo/" + "_search"
        query_args = self.queryMaker(searchType, searchText)
        request = urllib2.Request(url, query_args)
        result = urllib2.urlopen(request)
        parsedresult = json.loads(result.read())
        return parsedresult

    def queryMaker(self, searchType, searchText):
        params = '{}'
        if searchType == 'searchall':
            params = '{"from": 0,"size" : 61,"query":{"query_string":{"query":"' + searchText + '"}}}'
        if searchType == 'year':
            params = '{"from": 0,"size" : 61,"query":{"query_string":{"query":"' + searchText + '","fields":["Year"]}}}'
        if searchType == 'emptype':
            params = '{"from": 0,"size" : 61,"query":{"query_string":{"query":"' + searchText + '","fields":["Employee Type"]}}}'
        if searchType == 'cadre':
            params = '{"from": 0,"size" : 61,"query":{"query_string":{"query":"' + searchText + '","fields":["Cadre"]}}}'
        if searchType == 'noemp':
            params = '{"from": 0,"size" : 61,"query":{"query_string":{"query":"' + searchText + '","fields":["No of Employees"]}}}'
        return params

    def iterate_cursor(self, cursor):
    	l = []
        for record in cursor:
            l.append({'_id':record['_id'],'Year':record['Year'], 'Employee Type':record['Employee Type'], 'Cadre':record['Cadre'],
                      'No of Employees':record['No of Employees']})
    	return l