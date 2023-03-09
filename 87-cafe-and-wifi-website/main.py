from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cafe and Wifi Website"

if __name__ == '__main__':
    app.run(debug=True)