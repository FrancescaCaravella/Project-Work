from flask import Flask, jsonify
import requests

url = "https://dnaspaces.eu/api/location/v1"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYnkiOiJMb2NhdGlvbiIsInR5cGUiOiJCZWFyZXIiLCJ0ZW5hbnRJZCI6MTU0MjAsInVzZXJuYW1lIjoiYWxiYW5lc2VnaWFubHVjYUBob3RtYWlsLml0Iiwia2V5SWQiOiIwOWI4NjYzYi03OTE2LTRhZmItYjE3MS1lNzhjNGJlMzNmODgiLCJ1c2VySWQiOjE5MzU4LCJpYXQiOjE2MjM4MzUzNzksImV4cCI6MTY1NTM3MTM3OX0.pRGF5LLQhyU0APJcNDZCG0yzzUF_LlZyyG1fjkWb7j4'
}

app = Flask(__name__)

@app.route("/clients", methods = ['GET'])
def get_clients():
    response = requests.request("GET", url + "/clients", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/clients/count", methods = ['GET'])
def get_clients_count():
    response = requests.request("GET", url + "/clients/count", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/clients/floors", methods = ['GET'])
def get_clients_floors():
    response = requests.request("GET", url + "/clients/floors", headers=headers, data=payload)
    return jsonify(response.text)


if __name__ == "__main__":
    app.run(debug=True)