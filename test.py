from bs4 import BeautifulSoup
import pandas
import requests
import csv
import re

urlList = list()
statusCodeLust = list()
file = open("urlList.txt", 'r') 
for line in file:
    try:
        url = requests.get(line)
        urlList.append(line)
        statusCodeLust.append(url.status_code)
    except Exception:
        urlList.append(line)
        statusCodeLust.append("error")
        

for line in urlList:
    line.replace('\n', '/')

file.close()
df = pandas.DataFrame(data={"statusCode": statusCodeLust, "urlList": urlList})
df.to_csv("urlList.csv", sep=',',index=False)

