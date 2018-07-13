from bs4 import BeautifulSoup
import requests
import pandas
from pandas import DataFrame, merge, read_csv

df1 = read_csv('200urlList3.csv')
list1 = list()
formList = list()
list1 = df1.url

for line in list1:
    url = line
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        form = soup.find_all("form")
        if(len(form) != 0):
            formList.append(url)
            print(url)
    except Exception:
        pass
        

print("end")
df = pandas.DataFrame(data={"col1": formList})
df.to_csv("formList2.csv", sep=',',index=False)
