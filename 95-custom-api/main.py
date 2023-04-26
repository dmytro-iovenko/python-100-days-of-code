from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

ITBOOK_DB_SEARCH_URL = "https://api.itbook.store/1.0/"

##RENDER HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)