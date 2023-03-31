from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route("/")
def home():
    img = Image.open('dog.jpg')
    img = img.convert('RGB')
    width, height = img.size
    r_total = 0
    g_total = 0
    b_total = 0
    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1
    print()

    
    return f"Most Used color is ({r_total/count}, {g_total/count}, {b_total/count})"

if __name__ == "__main__":
    app.run(debug=True)