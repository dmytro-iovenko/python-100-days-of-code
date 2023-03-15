from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "c5e1d407e79c9b506d7f48d0677d9603"
Bootstrap(app)

class TaskForm(FlaskForm):
    hotspot = StringField("Name ...", validators=[DataRequired()])
    submit = SubmitField("Add task")

@app.route("/", methods=["GET", "POST"])
def home():
    form = TaskForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)