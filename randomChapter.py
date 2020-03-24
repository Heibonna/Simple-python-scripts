#! /usr/bin/python3
import requests 
import re
from bs4 import BeautifulSoup 

resp=requests.get('https://www.randombiblechapter.com/') 
    
if resp.status_code == 200: 
    number = re.compile(r'.\n')

    soup=BeautifulSoup(resp.text,'html.parser')     
    title=soup.find("div",{"id":"content"})

    print('\nHere is your random Bible chapter:', end=' ') 
    print(title.find("h2").get_text() + '\n') 

    title=soup.find("div",{"id":"bibleChapter"})

    for i in title.findAll("div",{"class":"verse"}):
        print(number.sub(' ', i.get_text()[1:]))
else: 
    print("Connection or server error")     
