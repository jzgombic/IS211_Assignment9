#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request as request
from bs4 import BeautifulSoup as bs


url = request.urlopen('http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices')
soup = bs(url, 'html.parser')
table = soup.find_all('tr')

def main():
    for row in table:
        td = row.find_all("td")

        try:
            date = str(td[0].get_text())
            closing = td[4].get_text()
            adjclosing = td[5].get_text()

        except:
            continue
    
        print ("Date: {}, Closing Price: ${}, Adjusted Closing: ${}".format(date, closing, adjclosing))


if __name__ == "__main__":
    main()
