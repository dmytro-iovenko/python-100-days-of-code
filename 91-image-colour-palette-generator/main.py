from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Image Colour Palette Generator"

if __name__ == "__main__":
    app.run(debug=True)