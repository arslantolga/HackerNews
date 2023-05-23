import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.content, "html.parser")

tr_class = soup.find_all("tr", class_= 'athing')
print("""
Program is over! 
"news.txt" created.
""")

with open("news.txt","w",encoding='UTF-8') as file:
    with open("news.txt", "a", encoding='UTF-8') as file:
        file.write("\nHacker top 30 news :\n\n")
    for a in tr_class:
        rank = a.find("span", class_="rank")
        for b in a.find("span", class_="titleline"):
            if not "." in b.text:
                with open("news.txt","a",encoding='UTF-8') as file:
                    new_text = rank.text + b.text
                    file.write(new_text + "\n")