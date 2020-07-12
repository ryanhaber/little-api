import flask
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/fish', methods=['GET'])
def fish():
	py_resource = {
		"name": {"first": "Ryan", "last": "Haber"},
		"age": 43,
		"rank": "space commander",
		"serialNumber": "00123",
		"pets": [{
			"name": "Goldilocks",
			"type": "fish"
			},
			{"name": "Sherlock",
			"type": "foxhound"}
		]
	}
	json_resource = json.dumps(py_resource)
	return(json_resource)


app.run()