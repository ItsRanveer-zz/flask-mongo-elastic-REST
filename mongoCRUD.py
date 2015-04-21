__author__ = 'ranveer'

import sys
from bson.objectid import ObjectId
from bson.json_util import dumps

class MongoCRUD:

    # Constructor for the class
    def __init__(self, database):
        self.db = database
        self.drdo = database.drdo

    def findAll(self):
    	cursor = self.drdo.find()
    	return self.iterate_cursor(cursor)

    def insert_new(self, year, emptype, cadre, noemp):
        data = {"Year": year,
                "Employee Type": emptype,
                "Cadre": cadre,
                "No of Employees":noemp}
        record = self.drdo.insert(data)
        data['_id'] = record
        return data

    def update_old(self, objectId, year, emptype, cadre, noemp):
    	query = {}
    	if year != "":
    		query['Year'] = year
    	if emptype != "":
    		query['Employee Type'] = emptype
    	if cadre != "":
    		query['Cadre'] = cadre
    	if noemp != "":
    		query['No of Employees'] = noemp
        record = self.drdo.update({'_id': ObjectId(objectId)}, {'$set': query})
        
        if record['updatedExisting'] == True and record['ok'] == 1:
        	msg = "Updated SuccessFully"
        else:
        	msg = "Cannot Update"
        return msg

    def remove(self, objectId):
        record = self.drdo.remove({'_id': ObjectId(objectId)})
        if record['ok'] == 1 and record['n'] == 1:
        	msg = "Deleted SuccessFully"
        elif record['ok'] == 1 and record['n'] == 0:
            msg = "No Record Found for this Id"
        else:
        	msg = "Cannot Delete"
        return msg

    def query(self, option, query):
        if query == "":
            query = "{}"
        if option == "update":
            query = "{},{}"
        final = "self.drdo." + option + "(" + query + ")"
        msg = eval(final)
        return dumps(msg)

    def iterate_cursor(self, cursor):
    	l = []
        for record in cursor:
            l.append({'_id':record['_id'],'Year':record['Year'], 'Employee Type':record['Employee Type'], 'Cadre':record['Cadre'],
                      'No of Employees':record['No of Employees']})
    	return l