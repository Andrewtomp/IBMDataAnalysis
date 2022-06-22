# uses data from provided url to create a csv file containing the technology language and average salary


# !pip3 install requests
# !pip3 install pandas
# !pip3 install beautifulsoup4
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
dataL = requests.get(url).text
soupL = BeautifulSoup(dataL, 'html.parser')

with open('popular-languages.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Language name', 'annual average salary'])
    for row in soupL.find_all("tbody")[0].find_all('tr'):
        col = row.find_all("td")
        lang = col[1].text
        salary = col[3].text
        writer.writerow([lang, salary])
    
