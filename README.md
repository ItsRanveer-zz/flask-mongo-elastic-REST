# flask-mongo-elastic-REST

A REST project for CRUD operations made using Flask, Mongo and Elastic

This project covers making a small REST website for CRUD operations using:

* Flask (a python microframework).
* MongoDB (a document database), used for storing the data.
* Elastic (search server based on Lucene), used for indexing and searching the data.
* Bootstrap (front-end framework), for user interface.

## Run

For running this project first install Python, MongoDB, Pymongo, Flask and Elastic.
And make sure MongoDB is listening on port `27017` and Elastic on port `9200`.
Then move to `etlMongo` folder and run `etl.py`.

	python etl.py

This will insert some into MongoDB database, db name will be `gov` and collection name `drdo`.
Data will be inserted from `raw.json` file, which contains some random DRDO dataset containing four fields.
`Cadre`, `No of Employees`, `Employee Type`, `Year`.
While inserting into Mongo a `_id` field will be added which we can use as `Id` field.

Now move to `bulkElastic` folder and run `bulk.py`.

	python bulk.py

This will put data into Elastic with index name `drdoindex` and document type `drdo`.
It will use `data.txt` to index the data, which is the same dataset we used to insert into Mongo.

Now for running the application run `app.py`.

	python app.py

After running `app.py` your application will start listening on [http://localhost:5000/](http://localhost:5000/) and you should see Welcome screen.
From here you can use different buttons to do CRUD.
You can also login as admin using [http://localhost:5000/login/](http://localhost:5000/login/) (Username = admin, Password = admin) to see the Mongo query shell.
You can also perform search using Search button.