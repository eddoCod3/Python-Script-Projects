import requests
from bs4 import BeautifulSoup
import pdfkit
import os
from string import Template
import pywhatkit
from datetime import datetime
import time


t = Template('$x')
link = input("Link of the page : ")
page  = requests.get(link)
soup = BeautifulSoup(page.text , "html.parser")
item = soup.find("h1").text
content = soup.find(class_="crayons-article__main").text
full = item + content

seconds = time.time() + 80
date =datetime.fromtimestamp(seconds)
def remove(string):
    return string.replace(" ", "")
#print(item.encode("utf-8"))
#print(content.encode("utf-8"))

with open("file.txt", "w+", encoding="utf-8") as file:   #You need to specify the encoding to not get in to trouble
    file.write(full)

pdfkit.from_file("file.txt", "text_pdf.pdf")
os.startfile("text_pdf.pdf")


pywhatkit.sendwhatmsg("+xxxxxxxxxxx", full, date.hour, date.minute) #add your number 
# Substitute value of x in above template
print (   remove(t.substitute({'x' : item}))  )
