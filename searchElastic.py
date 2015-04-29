__author__ = 'ranveer'

import json
import urllib2

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