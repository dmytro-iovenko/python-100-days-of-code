import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text

job = "data+analyst"
location = "United+States"
url = "https://in.indeed.com/jobs?q="+job+"&l="+location

htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

print(soup.prettify())
