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
    title = StringField("", validators=[DataRequired()], render_kw={"placeholder": "Search..."})
    submit = SubmitField("Search")


##RENDER HOME PAGE
@app.route('/', methods=["GET", "POST"])
def home():
    form = FindBookForm()
    if form.validate_on_submit():
        return redirect(url_for("search", query=form.title.data))
    response = requests.get(ITBOOK_DB_NEWBOOKS_URL)
    new_books = response.json()["books"]
    return render_template("index.html", books=new_books, form=form)

@app.route('/search/')
@app.route('/search/<query>', methods=["GET", "POST"])
def search(query=None):
    if query is None:
        return redirect(url_for("home"))
    form = FindBookForm()
    if form.validate_on_submit():
        return redirect(url_for("search", query=form.title.data))
    response = requests.get(f"{ITBOOK_DB_SEARCH_URL}/query={query}")
    books = response.json()["books"]
    return render_template("search.html", books=books, form=form, query=query)


@app.route('/book/')
@app.route('/book/<int:book_id>', methods=["GET", "POST"])
def show_book(book_id=None):
    if book_id is None:
        return redirect(url_for("home"))
    form = RateBookForm(id=book_id)
    if form.validate_on_submit():
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


@app.route("/admin", methods=["GET", "POST"])
def admin():
    reviews = Review.query.all()
    return render_template("admin.html", reviews=reviews)


@app.route("/admin/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id=None):
    if review_id is None:
        return redirect(url_for("admin"))
    review = Review.query.get(review_id)
    form = RateBookForm(name=review.name, review=review.review, rate=review.rate)
    if form.validate_on_submit():
        review.name = form.name.data
        review.review = form.review.data
        review.date = datetime.datetime.now()
        review.rate = form.rate.data
        db.session.commit()
        return redirect(url_for("admin"))
    return render_template("edit.html", review=review, form=form)


@app.route("/admin/delete/<int:review_id>")
def delete_review(review_id=None):
    if review_id is None:
        return redirect(url_for("admin"))
    review = Review.query.get(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("admin"))


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)