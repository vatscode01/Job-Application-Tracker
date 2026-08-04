from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Job quest tracker is alive</h1>"


if (__name__ == "__main__"):
    app.run(debug=True)

###################

url = "http://127.0.0.1:5000/"

response = requests.get(url)

print(response)

