from flask import Flask,request, jsonify
import json
app = Flask(__name__)

@app.route("/")
def hello():
  return "hola mundo"

@app.route('/practica_uno/geojsonFile')
def getData():
  data = []
  
return jsonify(success=True, data=data)

if __name__ == "__main__":
app.run(host='localhost', port=5000, debug=True)
