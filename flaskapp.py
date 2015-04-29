__author__ = 'ranveer'

import pymongo
import mongoCRUD
import searchElastic
from flask import Flask, request, flash, url_for, redirect, render_template, abort, send_from_directory

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	page = 'index'
	return render_template('index.html', pageType = page)

@app.route('/result/showAll/', methods=["GET"])
def showAll():
	page = 'showAll'
	mongoData = mongoDBObj.findAll()
	return render_template('index.html', pageType = page , data = mongoData)

@app.route('/result/insert/', methods=["GET","POST"])
def insert():
	if request.method == "GET":
		page = 'insert'
		return render_template('insert.html', pageType = page)
	if request.method == "POST":
		year = request.form['year']
		emptype = request.form['emptype']
		cadre = request.form['cadre']
		noemp = request.form['noemp']
		mongoData = mongoDBObj.insert_new(year, emptype, cadre, noemp)
		page = 'inserted'
		return render_template('insert.html', pageType = page, data = mongoData)

@app.route('/result/update/', methods=["GET","POST"])
def update():
	if request.method == "GET":
		page = 'update'
		return render_template('update.html', pageType = page)
	if request.method == "POST":
		method = request.form['_method'].upper()
		if method == "PATCH":
			objectId = request.form['objectId']
			year = request.form['year']
			emptype = request.form['emptype']
			cadre = request.form['cadre']
			noemp = request.form['noemp']
			mongoMsg = mongoDBObj.update_old( objectId, year, emptype, cadre, noemp)
			page = 'updated'
			return render_template('update.html', pageType = page, data = mongoMsg)

@app.route('/result/delete/', methods=["GET","POST"])
def delete():
	if request.method == "GET":
		page = 'delete'
		return render_template('delete.html', pageType = page)
	if request.method == "POST":
		method = request.form['_method'].upper()
		if method == "DELETE":
			objectId = request.form['objectId']
			mongoMsg = mongoDBObj.remove(objectId)
			page = 'deleted'
			return render_template('delete.html', pageType = page, data = mongoMsg)

@app.route('/searchfilter/', methods=["GET","POST"])
def searchfilter():
	if request.method == "GET":
		page = 'snf'
		return render_template('search.html', pageType = page)
	if request.method == "POST":
		page = 'snfresult'
		searchType = request.form['searchType']
		searchText = request.form[searchType]
		result = elasticObj.search(searchType, searchText)
		return render_template('search.html', pageType = page, data = result)

@app.route("/login/", methods=["GET", "POST"])
def login():
	msg = ""
	if request.method == "GET":
		page = 'login'
		return render_template('login.html', pageType = page, data = msg)
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		if username == 'admin' and password == 'admin':
			page = 'loggedin'
			return redirect(url_for('shell', Username = username, Password = password))
		else:
			page = 'login'
			msg = 'Wrong User Name or Password. Try Again'
			return render_template('login.html', pageType = page, data = msg)

@app.route("/shell/", methods=["GET", "POST"])
def shell():
	username = request.args.get('Username')
	password = request.args.get('Password')
	if username != 'admin' or password != 'admin':
		abort(403)
	if request.method == "GET":
		page = 'shell'
		return render_template('shell.html', pageType = page)
	if request.method == "POST":
		page = 'shell'
		option = request.form['optradio']
		query = request.form['query']
		mongoMsg = mongoDBObj.query(option, query)
		return render_template('shell.html', pageType = page, data = mongoMsg, Username = username, Password = password)

@app.route("/test/", methods=["GET"])
def test():
    return "<strong>I am On!</strong>"

@app.route('/<path:resource>', methods=["GET"])
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# Mongo Connect
connection = pymongo.MongoClient(host="mongodb://localhost:27017")
database = connection.gov
mongoDBObj = mongoCRUD.MongoCRUD(database)

# Elastic Connect
elasticHost = "http://localhost:9200"
elasticObj = searchElastic.SearchElastic(host=elasticHost)

if __name__ == '__main__':
    app.run()