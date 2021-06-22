from flask import Flask, jsonify
import requests

url = "https://dnaspaces.eu/api/location/v1"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYnkiOiJMb2NhdGlvbiIsInR5cGUiOiJCZWFyZXIiLCJ0ZW5hbnRJZCI6MTU0MjAsInVzZXJuYW1lIjoiYWxiYW5lc2VnaWFubHVjYUBob3RtYWlsLml0Iiwia2V5SWQiOiIwOWI4NjYzYi03OTE2LTRhZmItYjE3MS1lNzhjNGJlMzNmODgiLCJ1c2VySWQiOjE5MzU4LCJpYXQiOjE2MjM4MzUzNzksImV4cCI6MTY1NTM3MTM3OX0.pRGF5LLQhyU0APJcNDZCG0yzzUF_LlZyyG1fjkWb7j4'
}

app = Flask(__name__)

@app.route("/map/hierarchy", methods = ['GET'])
def get_map_hierarchy():
    response = requests.request("GET", url + "/map/hierarchy", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/map/elements/<elementId>", methods = ['GET'])
def get_map_elements(elementId):
    response = requests.request("GET", url + "/map/elements/{elementId}", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/map/images/floor/<imageName>", methods = ['GET'])
def get_map_images_floor(imageName):
    response = requests.request("GET", url + "/map/images/floor/{imageName}", headers=headers, data=payload)
    return jsonify(response.text)

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

@app.route("/accessPoints", methods = ['GET'])
def get_accessPoints():
    response = requests.request("GET", url + "/accessPoints", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/accessPoints/count", methods = ['GET'])
def get_accessPoints_count():
    response = requests.request("GET", url + "/accessPoints/count", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/accessPoints/list", methods = ['GET'])
def get_accessPoints_list():
    response = requests.request("GET", url + "/accessPoints/list", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/history", methods = ['GET'])
def get_history():
    response = requests.request("GET", url + "/history", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/history/records/count", methods = ['GET'])
def get_history_records_count():
    response = requests.request("GET", url + "/history/records/count", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/history/records", methods = ['GET'])
def get_history_records():
    response = requests.request("GET", url + "/history/records", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/history/clients", methods = ['GET'])
def get_history_clients():
    response = requests.request("GET", url + "/history/clients", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/history/clients/<deviceId>", methods = ['GET'])
def get_history_clients_deviceId(deviceId):
    response = requests.request("GET", url + "/history/clients/{deviceId}", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/notifications", methods = ['GET'])
def get_notifications():
    response = requests.request("GET", url + "/notifications", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/notifications/<subscriptionId>", methods = ['GET'])
def get_notifications_subscriptionId(subscriptionId):
    response = requests.request("GET", url + "/notifications/{subscriptionId}", headers=headers, data=payload)
    return jsonify(response.text)

@app.route("/notifications/subscriptionId/statistics", methods = ['GET'])
def get_notifications_subscriptionId_statistics():
    response = requests.request("GET", url + "/notifications/subscriptionId/statistics", headers=headers, data=payload)
    return jsonify(response.text)


if __name__ == "__main__":
    app.run(debug=True)
