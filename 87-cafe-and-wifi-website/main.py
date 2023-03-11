from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import csv

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hotspots")
def hotspots():
    with open("free-public-wifi-hotspots.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=";")
        header_row = next(csv_data)  # get the headers
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("hotspots.html", hotspots=list_of_rows, header=header_row)

if __name__ == "__main__":
    app.run(debug=True)