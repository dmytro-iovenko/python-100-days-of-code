from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import requests
import datetime

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
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn13 = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    review = db.Column(db.String(2000), nullable=True)
    rate = db.Column(db.Integer, nullable=False)

db.create_all()


class RateBookForm(FlaskForm):
    name = StringField("", validators=[DataRequired()], render_kw={"placeholder": "Your name"})
    review = TextAreaField("", validators=[DataRequired()], render_kw={"placeholder": "Enter your review...", "maxLength": "2000", "spellcheck": "false"})
    rate = StringField("", validators=[DataRequired()], render_kw={"placeholder": "Rate from 1 to 5"})
    id = HiddenField()
    submit = SubmitField("Submit Review")
    

class FindBookForm(FlaskForm):
    title = StringField("Book Title", validators=[DataRequired()])
    submit = SubmitField("Add Book")


##RENDER HOME PAGE
@app.route('/')
def home():
    response = requests.get(ITBOOK_DB_NEWBOOKS_URL)
    new_books = response.json()["books"]
    return render_template("index.html", books=new_books)


@app.route('/book', methods=["GET", "POST"])
def show_book():
    book_id = request.args.get("id")
    form = RateBookForm(id=book_id)
    if form.validate_on_submit():
        print(book_id)
        print(form)
        review = Review(
            isbn13 = book_id,
            name = form.name.data,
            date = datetime.datetime.now(),
            review = form.review.data,
            rate = form.rate.data
        )
        db.session.add(review)
        db.session.commit()
        form = RateBookForm(formdata=None, id=book_id)
    response = requests.get(f"{ITBOOK_DB_INFO_URL}/{book_id}")
    book = response.json()
    reviews = Review.query.filter(Review.isbn13 == book_id).all()
    return render_template("book.html", book=book, form=form, reviews=reviews)


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