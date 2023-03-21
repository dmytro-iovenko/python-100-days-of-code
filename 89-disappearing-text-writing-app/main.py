from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField

app = Flask(__name__)
app.config["SECRET_KEY"] = "aa2e8495eae2e6e7f103e745855a926d"
Bootstrap(app)

class EditForm(FlaskForm):
    text = TextAreaField("", render_kw={"placeholder": "Start typing...", "spellcheck": "false"})

@app.route("/")
def home():
    form = EditForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)