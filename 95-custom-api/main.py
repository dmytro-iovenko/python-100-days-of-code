from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b6f9aff3cbefb58d0cd90906864ed4a3'
Bootstrap(app)

ITBOOK_DB_SEARCH_URL = "https://api.itbook.store/1.0/search"

class FindBookForm(FlaskForm):
    title = StringField("Book Title", validators=[DataRequired()])
    submit = SubmitField("Add Book")


##RENDER HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_book():
    form = FindBookForm()
    if form.validate_on_submit():
        book_title = form.title.data
        response = requests.get(f"{ITBOOK_DB_SEARCH_URL}/query={book_title}")
        data = response.json()["books"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)