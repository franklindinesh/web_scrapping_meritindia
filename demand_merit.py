import requests as req
import re
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import datetime as dt
from datetime import date
from datetime import datetime

link = "https://meritindia.in/state-data/tamil-nadu"
Web = req.get(link)
soup = BeautifulSoup(Web.content, 'html.parser')
divs = soup.find(class_="map_details_section_image")
AllIndiaDemand = soup.find_all('input', {'id': 'AllIndiaDemand'})
ISGSGen = soup.find_all('input', {'id': 'ISGSGen'})
Import_data = soup.find_all('input', {'id': 'Import_data'})

with open('meritdatassss444_25052023.csv', 'w', encoding='utf-16le', newline='') as f:
    thewriter = writer(f)
    header = ['Date','Demand Met', 'Own Gerneration', 'Import ', 'Rec. Time']
    thewriter.writerow(header)

    p = 0
    a = []
    while True:
        try:
            today = date.today()
            print("Date            : ", today)

            reqs = requests.get(link)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            #print(soup)

            # TN_DEMAND = AllIndiaDemand[0]['value']
            # print("Demand Met     : ",TN_DEMAND)

            for i in soup.find_all('input', {'id': 'AllIndiaDemand'}):
                print("Demand Met      : ",i['value'])

            for j in soup.find_all('input', {'id': 'ISGSGen'}):
                print("Own Gerneration : ",j['value'])

            for k in soup.find_all('input', {'id': 'Import_data'}):
                print("Import          : ",k['value'])


    # INT_TN_DEMAND = ''.join(x for x in TN_DEMAND if x.isdigit())
    # print(INT_TN_DEMAND)

    # TN_GEN = ISGSGen[0]['value']
    # print("Own generation : ",TN_GEN)
    # #INT_TN_GEN = ''.join(x for x in TN_GEN if x.isdigit())
    # #print(INT_TN_GEN)
    #
    # TN_IMP = Import_data[0]['value']
    # print("Import         : ",TN_IMP)
    # #INT_TN_IMP = ''.join(x for x in TN_IMP if x.isdigit())
    # #print(INT_TN_IMP)
    #
            now = datetime.now()
    # print("now =", now)
    # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Rec. Time       : ", dt_string)

            print("----------------------------------------")

            time.sleep(300)

            if i == 5000:
                break
            p = p + 1
            a = [p]
            print(a)

            info = [today, i['value'], j['value'],k['value'],dt_string]
            thewriter.writerow(info)
        except:
            print("No connection")

    #print(INT_TN_DEMAND+", "+INT_TN_GEN+", "+INT_TN_IMP)
























'''
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import datetime as dt
from datetime import date
from datetime import datetime
from datetime import date
from datetime import datetime

url = "https://meritindia.in/state-data/tamil-nadu"
page = requests.get(url)
#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
i = 0
a = []
while True:
    today = date.today()
    print(" Date         : ", today)
    lists = soup.find_all('div', class_="map_details_section_image")
#print(lists)
    head = soup.find_all('input', {'id': 'AllIndiaDemand'})
    print(head[0]['value'])

    tail = soup.find_all('input', {'id': 'ISGSGen'})
    print(head[0]['value'])

    print("-----------------------------------------------")
    time.sleep(60)

    if i == 5000:
        break
    i = i + 1
    a = [i]
    print(a)'''




