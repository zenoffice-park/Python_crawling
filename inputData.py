from bs4 import BeautifulSoup
import requests
import pandas
from pandas import DataFrame, merge, read_csv
import urllib.request
import codecs
import csv
########################### Save Html To Local #############################################################
url = list()
statusCode = list()
df1 = read_csv('formList.csv')
url = df1.url
i = 1

for line in url:
    try:
        request = requests.get(line)
    except Exception:
        pass
    soup = BeautifulSoup(request.text, 'html.parser')
    try:
        open("./html/htmlFIle-"+str(i)+".txt", "wb").write(urllib.request.urlopen(line).read())
    except Exception:
        pass
    
    i = i + 1


print("end")

########################### Fine Form #############################################################


inputTagList = list()
Dic = {'url': 'tagList'}
k = 0

for j in range(1, i-1):
    with codecs.open("./html/htmlFIle-"+str(j)+".txt", 'r', encoding='utf8') as fp:
        try:
            soup2 = BeautifulSoup(fp, 'html.parser')
            inputTagList = soup2.find_all('input')
            Dic[df1.url[k].strip()] = inputTagList
            k = k + 1
        except Exception:
            pass

print(Dic)


######################################################################## 특정 태그의 속성값 리스팅


inputTagList = list()
inputTagList2 = list()
inputTagList3 = list()
Dic = {'url': 'tagList'}
k = 0

for j in range(1, i-1):
    with codecs.open("./html/htmlFIle-"+str(j)+".txt", 'r', encoding='utf8') as fp:
        try:
            soup2 = BeautifulSoup(fp, 'html.parser')
            inputTagList = soup2.find_all('form')
            for form in inputTagList:
                inputTagList2 = form.find_all('input')
                for inputTag in inputTagList2:
                    inputTagList3.append(inputTag.get('name'))
        except Exception:
            pass

print(len(inputTagList3))
s1 = list(set(inputTagList3))
print(s1)





with open("./html/List.csv", 'a') as outcsv:   
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['name'])
    for item in s1:
        writer.writerow([item[0]])