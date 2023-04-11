import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from urllib.parse import quote_plus

def getdata(url, header):
    r = requests.get(url, headers=header)
    return r.text

def job_data(soup):
    data_str = ""
    for item in soup.find_all("a", class_="jobtitle turnstileLink"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    return(result_1)

def company_data(soup):
    data_str = ""
    result = ""
    for item in soup.find_all("div", class_="sjcl"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    res = []
    for i in range(1, len(result_1)):
        if len(result_1[i]) > 1:
            res.append(result_1[i])
    return(res)


class SearchForm(FlaskForm):
    job = StringField("What", validators=[DataRequired()], render_kw={"placeholder": "Job title, keywords, or company"})
    location = StringField("Where", validators=[DataRequired()], render_kw={"placeholder": "City, state, zip code, or 'remote'"})
    submit = SubmitField("Search Job")


app = Flask(__name__)
app.config["SECRET_KEY"] = "f7dd50b017d598db4b7c84c2d80c7441"
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
    }

    form = SearchForm()
    result = []

    if form.validate_on_submit():
        job = quote_plus(form.job.data)
        location = quote_plus(form.location.data)
        url = "https://indeed.com/jobs?q="+job+"&l="+location

        htmldata = getdata(url, header)
        soup = BeautifulSoup(htmldata, 'html.parser')

        job_res = job_data(soup)
        com_res = company_data(soup)
        
        temp = 0
        for i in range(1, len(job_res)):
            job_info = []
            j = temp
            for j in range(temp, 2+temp):
                job_info.append(com_res[j])
            temp = j
            job_info = job_info.append(job_res[i])
            result.append(job_info)

    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=True)