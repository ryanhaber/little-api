import flask
from flask import render_template
import json
import pymongo

# client = pymongo.MongoClient(
#    "mongodb+srv://ryanhaber:ryanhaber@localhost:27017/test?retryWrites=true&w=majority")
# db = client.test

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/fish/', methods=['GET'])
@app.route('/fish/<path:fishname>', methods=['GET'])
def show_subpath(fishname=None):
	if not fishname:
		return "1"
	else:
		return render_template('fishfact.html', name=fishname)

	
app.run()