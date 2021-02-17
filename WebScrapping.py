import requests
from bs4 import BeautifulSoup
quotes=[]  # a list to store quotes
url='https://www.airport-jfk.com/departures.php'
#params ={'flight-col flight-col__dest-term'}
page = requests.get('https://www.airport-jfk.com/departures.php')

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all(class_='flight-row')
for row in table:
    if(row.attrs=={'class_': ['flight-col flight-col__dest-term']}==True):
        print(row)
    quote = {}
    line = row.text
    line = line.replace('\t',' ')
    line = line.replace('\n','')
    #quote = row.text.rstrip("\n")
    #quote = line
    quotes.append(line)

print(quotes)