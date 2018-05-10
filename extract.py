# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

class Notice:
    IDNumbers = []
    URLs = []
    Titles = []
    Dates = []

    def __init__(self):
        url = 'http://dormitory.cau.ac.kr/bbs/bbs_list.php?bbsID=notice'
        source = requests.get(url)
        source.encoding = None
        text_file = source.text

        for detail in BeautifulSoup(text_file, 'html.parser').find_all("tr", {"bgcolor": "#fffcdb"}):
            menuSoup = BeautifulSoup(str(detail), 'html.parser')
            URL = menuSoup.find('a')['href']
            URL = str(URL).replace("s", "", 1)
            detailSource = requests.get(URL)
            detailSource.encoding = None

            # Number Parsing
            self.IDNumbers.append(noticeNum(detailSource.text))
            #URL Parsing
            self.URLs.append(URL)
            # Title Parsing
            self.Titles.append(noticeTitle(detailSource.text))
            # Date Parsing
            self.Dates.append(noticeDate(detailSource.text))

def noticeNum(url):
    htmlSoup = BeautifulSoup(url, 'html.parser')
    number = htmlSoup.find_all("td", {"class": "v_t"})[0].text
    result = re.findall("\d\d\d\d", str(number))[0]
    return result

def noticeTitle(url):
    htmlSoup = BeautifulSoup(url, 'html.parser')
    title = htmlSoup.find_all("td", {"class": "bold f14"})[0].text
    result = str(title).replace("제목 : ", "", 1)
    return result

def noticeDate(url):
    htmlSoup = BeautifulSoup(url, 'html.parser')
    title = htmlSoup.find_all("td", {"class": "f11 t_r"})[0].text
    result = str(title).replace(" by 생활관", "", 1)
    return result

def noticeDetailHTML(url):
    htmlSoup = BeautifulSoup(url, 'html.parser')
    tableSource = htmlSoup.find_all("table", {"class": "tbl_board"})[1]
    tableSoup = BeautifulSoup(str(tableSource), 'html.parser')
    result = tableSoup.find_all("tr")[5]
    return result