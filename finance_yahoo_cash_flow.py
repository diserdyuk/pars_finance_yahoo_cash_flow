import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)    
    return r.text


def write_csv(d):
    with open('finance_yahoo_cash_flow_AAPL.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((d['name'], d['ttm'], d['year_2019'], d['year_2018'], d['year_2017']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    tbrs = soup.find('div', class_= 'D(tbrg)').find_all('div', class_='D(tbr)')

    for tbr in tbrs:
        tb = tbr.find_all('div')
        
        try:
            name = tb[0].find('span').text
        except:
            name = ''

        try:
            ttm = tb[3].find('span').text.replace(',','.') 
        except:
            ttm = '-'
            
        try:
            year_2019 = tb[4].find('span').text.replace(',','.')
        except:
            year_2019 = '-'

        try:
            year_2018 = tb[5].find('span').text.replace(',','.')
        except:
            year_2018 = '-'

        try:
            year_2017 = tb[6].find('span').text.replace(',','.')
        except:
            year_2017 = '-'

        data = {'name': name, 'ttm': ttm, 'year_2019': year_2019, 'year_2018': year_2018, 'year_2017': year_2017}
        write_csv(data)
        

def main():
    # url = 'https://finance.yahoo.com/quote/GOOG/cash-flow?p=GOOG'
    url = 'https://finance.yahoo.com/quote/aapl/cash-flow?p=AAPL'
    get_data(get_html(url))

if __name__ == '__main__':
    main()