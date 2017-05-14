import requests
import pandas
import time
from bs4 import BeautifulSoup

BASE_URL = 'http://www.nuforc.org/webreports/ndxe{}.html'
COLUMNS = ['datetime', 'city', 'state', 'shape', 'duration', 'summary', 'posted']

table = []

# sub-10 months need to be prepended with a zero (ie 05 )
year = 1979
month = 1

frame = pandas.DataFrame()

while ( year != 2008 ):

    # create year/month string 
    formatted_date = '{}0{}'.format(year, month) if month < 10 else '{}{}'.format(year, month)

    # fetch page
    page = requests.get( BASE_URL.format( formatted_date ))

    # parse page and get table
    soup = BeautifulSoup(page.content, 'html.parser')

    # get rows from table and write to memory
    for row in soup.find_all('tr')[1:]:
        table.append([cell.text for cell in row.find_all('td')])


    print('Read: {}-{}'.format(year, month))

    # Increment Month
    month = month + 1 if month < 12 else 1
    year = year + 1 if month == 1 else year

    # Give the site a break
    time.sleep(1)


frame = pandas.DataFrame( table, columns = COLUMNS )
frame.to_csv('sightings.csv', index = False, sep='|')