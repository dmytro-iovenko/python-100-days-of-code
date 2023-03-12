from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "9d755d0dd6bc0a35cd77ed4c0b4e1ca2"
Bootstrap(app)

class HotspotForm(FlaskForm):
    hotspot = StringField("Hotspot Name", validators=[DataRequired()])
    type = SelectField("Hotspot Type", choices=["Kiosk", "Library", "Cafe"], validators=[DataRequired()])
    address = StringField("Street Address", validators=[DataRequired()])
    latitude = StringField("Latitude", validators=[DataRequired()])
    longitude = StringField("Longitude", validators=[DataRequired()])
    submit = SubmitField('Submit')

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

@app.route('/add', methods=["GET", "POST"])
def add_hotspot():
    form = HotspotForm()
    if form.validate_on_submit():
        with open("free-public-wifi-hotspots.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.hotspot.data};"
                           f"{form.type.data};"
                           f"{form.address.data};"
                           f"{form.latitude.data};"
                           f"{form.longitude.data};"
                           f"{form.latitude.data}, {form.longitude.data}")
        return redirect(url_for('hotspots'))
    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)