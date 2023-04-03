from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from PIL import Image
import base64
import io

app = Flask(__name__)
app.config["SECRET_KEY"] = "404d78ae5d0e579fa43f1d43ccb31c17"
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        if "image" in request.files:
            # get image
            img_file = request.files["image"]

            img = Image.open(img_file)
        
            img = img.convert('RGB')
            width, height = img.size

            data = io.BytesIO()
            img.save(data, "JPEG")
            encoded_img_data = base64.b64encode(data.getvalue())
        
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
            result = f"{round(r_total/count)}, {round(g_total/count)}, {round(b_total/count)}"
	
            return render_template("index.html", img_data=encoded_img_data.decode('utf-8'), title=f"Most Used color is RGB({result})", color=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)