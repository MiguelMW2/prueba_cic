from flask import Flask,request, jsonify
import json
app = Flask(__name__)

@app.route("/")
def hello():
  return "hola mundo"

@app.route('/getData/<name>')
def getData(name):

  print (name)
  data = [[1, 2, 3], {"a": 1, "b": 2}, name]
  diccionario = {
     1: [{ "num1" : 1 }],
     2: [{ "Letra1" : "A" }],
     3: [{
        "data1" : 1,
        "data2" : 2,
         "data3": 3,
         "data4" : ["a","b","c","d",("tup1", "tup2")]
     }]
  }
  #return json.dumps("Respuesta")

  return jsonify(success=True, data=data)

@app.route('/data' ,  methods=['POST'])
def getDataFromFunction():

  a = request.get_json()

  print ("res: ",a)

  data = [[1,2,3],{"a":1,"b":2}, a]
  #return json.dumps("answer")
  return jsonify(success=True, data=data)

if __name__ == "__main__":
  app.run(host='localhost', port=5000, debug=True)
