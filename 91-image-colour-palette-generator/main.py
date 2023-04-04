from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
from PIL import Image
import matplotlib.image as img
import matplotlib.pyplot as plt
import pandas as pd
import base64
import io

app = Flask(__name__)
app.config["SECRET_KEY"] = "404d78ae5d0e579fa43f1d43ccb31c17"
Bootstrap(app)

plt.switch_backend('agg')

def fig_to_base64(fig):
    tmp_img = io.BytesIO()
    fig.savefig(tmp_img, format='jpeg',
                bbox_inches='tight')
    return base64.b64encode(tmp_img.getvalue())

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
        
            r = []
            g = []
            b = []

            for x in range(0, width):
                for y in range(0, height):
                    temp_r, temp_g, temp_b = img.getpixel((x,y))
                    r.append(temp_r)
                    g.append(temp_g)
                    b.append(temp_b)

            img_df = pd.DataFrame({'red' : r,
                                   'green' : g,
                                   'blue' : b})

            img_df['scaled_color_red'] = whiten(img_df['red'])
            img_df['scaled_color_blue'] = whiten(img_df['blue'])
            img_df['scaled_color_green'] = whiten(img_df['green'])

            cluster_centers, _ = kmeans(img_df[['scaled_color_red',
                                                'scaled_color_blue',
                                                'scaled_color_green']], 3)

            dominant_colors = []
 
            red_std, green_std, blue_std = img_df[['red',
                                                   'green',
                                                   'blue']].std()

            for cluster_center in cluster_centers:
                red_scaled, green_scaled, blue_scaled = cluster_center
                dominant_colors.append((
                    red_scaled * red_std / 255,
                    green_scaled * green_std / 255,
                    blue_scaled * blue_std / 255
                ))

            plt.imshow([dominant_colors])

            return render_template("index.html", img_data=encoded_img_data.decode('utf-8'), color_data=fig_to_base64(plt).decode('utf-8'))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)