#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request as request
from bs4 import BeautifulSoup as bs


url = request.urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns')
soup = bs(url, 'html.parser')
table = soup.find_all("table", attrs={"class":"data"})[0].find_all("tr", attrs={"valign":"top"})


def main():

    print ("\nThe touchdown leaders are as follows:")

    count = 0

    for row in table:
        if count <= 19:
            name = row.find_all('td')[0].find_all('a')[0].contents[0]
            position = row.find_all('td')[1].contents[0]
            team = row.find_all('td')[2].find_all('a')[0].contents[0]
            touchdowns = row.find_all('td')[6].contents[0]
            count += 1
            print ("     {}.  {}, {}, {}, {}".format(count, name, team, position, touchdowns))


if __name__ == "__main__":
    main()
