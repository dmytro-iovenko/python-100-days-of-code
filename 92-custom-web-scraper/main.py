import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

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

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():

    job = "data+analyst"
    location = "United+States"
    url = "https://in.indeed.com/jobs?q="+job+"&l="+location

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
    }

    htmldata = getdata(url, header)
    soup = BeautifulSoup(htmldata, 'html.parser')

    job_res = job_data(soup)
    com_res = company_data(soup)

    temp = 0
    for i in range(1, len(job_res)):
        j = temp
        for j in range(temp, 2+temp):
            print("Company Name and Address : " + com_res[j])
        temp = j
        print("Job : " + job_res[i])
        print("-----------------------------")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)