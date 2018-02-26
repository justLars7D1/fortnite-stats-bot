from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://fortnitestats.net/stats/AshinGod'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "lxml")

try: 
    overall_stats = soup.find_all('h3')
    counter = 0
    for value in overall_stats:
        if counter < 6:
            overall_stats[counter] = str(overall_stats[counter]).replace('<h3>', '')
            overall_stats[counter] = str(overall_stats[counter]).replace('</h3>', '')
        counter = counter + 1  
        
    #overall_stats
    
    specific_stats = soup.find_all('p')
    counter = 7
    while counter > 6 and counter < 28:
        specific_stats[counter] = (str(specific_stats[counter]).replace('<p>', '').replace('</p>', ''))
        counter = counter + 1
    
    specific_stats
except:
    print('No user!')

soup

