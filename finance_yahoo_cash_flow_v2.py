import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)    
    return r.text


def write_csv(d):
    with open('finance_yahoo_cash_flow_GOOG_2.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((d['name'], d['ttm'], d['year_2019'], d['year_2018'], d['year_2017']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    tbrs = soup.find('div', class_= 'D(tbrg)').find_all('div', class_='D(tbr)')

    for tbr in tbrs:
        tb = tbr.find_all('div')
        
        data = {}
        schema = (("name", '', 0), ("ttm", "-", 3), ("year_2019", "-", 4), ("year_2018", "-", 5), ("year_2017", "-", 6)) # ((field, default_value), ...)
        
        for i in schema:
            field, default_value, nums = i
            
            try:
                data[field] = tb[nums].find('span').text.replace(',','.')
            except:
                data[field] = default_value

        write_csv(data)
        

def main():
    url = 'https://finance.yahoo.com/quote/GOOG/cash-flow?p=GOOG'
    # url = 'https://finance.yahoo.com/quote/aapl/cash-flow?p=AAPL'
    get_data(get_html(url))

if __name__ == '__main__':
    main()