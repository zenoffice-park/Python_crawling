from bs4 import BeautifulSoup
import pandas
import requests
import csv
import re

urlList = list()
statusCodeLust = list()
file = open("200urlList.csv", 'r') 
for line in file:
    try:
        url = requests.get(line)
        urlList.append(line)
        statusCodeLust.append(url.status_code)
    except Exception:
        urlList.append(line)
        statusCodeLust.append("error")
        

file.close()
df = pandas.DataFrame(data={"col1": urlList, "col2": statusCodeLust})
df.to_csv("urlList.csv", sep=',',index=False)