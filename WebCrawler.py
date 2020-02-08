import requests
url = "https://theinternship.io/"
data = requests.get(url)
from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text,'html.parser')
data_select = soup.find_all("div",{"class":"partner"})

lst = []
for i in data_select:
    company = i.select_one(".box-textbox span").text
    logo = i.select_one(".logo-box img")["src"]
    dic = {"company":company, "logo":logo}
    lst.append(dic)
lst.sort(key=lambda k : len(k['company']))
for i in lst:
    print(i.get('logo'))