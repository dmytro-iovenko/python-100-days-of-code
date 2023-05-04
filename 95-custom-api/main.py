from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b6f9aff3cbefb58d0cd90906864ed4a3'
Bootstrap(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

ITBOOK_DB_NEWBOOKS_URL = "https://api.itbook.store/1.0/new"
ITBOOK_DB_SEARCH_URL = "https://api.itbook.store/1.0/search"
ITBOOK_DB_INFO_URL = "https://api.itbook.store/1.0/books"

##CREATE TABLE
class Book(db.Model):
    isbn13 = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    authors = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
db.create_all()


class RateBookForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")
    

class FindBookForm(FlaskForm):
    title = StringField("Book Title", validators=[DataRequired()])
    submit = SubmitField("Add Book")


##RENDER HOME PAGE
@app.route('/')
def home():
    response = requests.get(ITBOOK_DB_NEWBOOKS_URL)
    new_books = response.json()["books"]
    return render_template("index.html", books=new_books)


@app.route('/book')
def show_book():
    book_id = request.args.get("id")
    return ""


@app.route("/edit", methods=["GET", "POST"])
def rate_book():
    form = RateBookForm()
    book_id = request.args.get("id")
    book = Book.query.get(book_id)
    if form.validate_on_submit():
        book.rating = float(form.rating.data)
        book.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book, form=form)


@app.route("/delete")
def delete_book():
    book_id = request.args.get("id")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_book():
    form = FindBookForm()
    if form.validate_on_submit():
        book_title = form.title.data
        response = requests.get(f"{ITBOOK_DB_SEARCH_URL}/query={book_title}")
        data = response.json()["books"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_book():
    book_api_id = request.args.get("id")
    if book_api_id:
        book_api_url = f"{ITBOOK_DB_INFO_URL}/{book_api_id}"
        response = requests.get(book_api_url)
        data = response.json()
        new_book = Book(
            isbn13=data["isbn13"],
            title=data["title"],
            authors=data["authors"],
            year=data["year"],
            rating=data["rating"],
            img_url=data["image"],
            description=data["desc"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)