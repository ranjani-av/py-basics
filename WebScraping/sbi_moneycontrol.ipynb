from bs4 import BeautifulSoup  #makes it easy for us to parse our html files we get from our requests
import requests
import csv


my_url = "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"
response = requests.get(my_url)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

heading = soup.title.text
title1 = heading[:20]

print(title1)
area_scrip=soup.find('div', class_= 'FL gry10')
b=area_scrip.text[12:19]
n=area_scrip.text[33:37]
#print(n+" | "+b+" |")


"""[<div class="FL PR5 gD_30" id="Bse_Prc_tick_div"><span id="Bse_Prc_tick"><strong>372.15</strong></span></div>,
<div class="FL PR5 gD_30" id="Nse_Prc_tick_div"><span class="PA2" id="Nse_Prc_tick"><strong>372.40</strong></span></div>]
"""
#for area in soup.find_all('div', class_= 'FL PR5 gD_30'):
    #print(area.text, end="    |    ")

price=[]

area = soup.find_all('div', class_= 'FL PR5 gD_30')
for i in area:
  a=i.text
  price.append(a)


with open('sbi.csv', 'w', newline= '') as f:
    f_names=['Stock Exchange', 'Scrip Code', 'Share Price']
    thewriter = csv.DictWriter(f, fieldnames=f_names)

    thewriter.writeheader()
    thewriter.writerow({'Stock Exchange': 'NSE', 'Share Price': price[0], 'Scrip Code': n})
    thewriter.writerow({'Stock Exchange': 'BSE', 'Share Price': price[1], 'Scrip Code': b})

