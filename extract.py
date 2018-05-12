# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import chardet
import sys

class Notice:
    IDNumbers = []
    Titles = []
    Dates = []

    def __init__(self):

        url = 'http://dormitory.cau.ac.kr/bbs/bbs_list.php?bbsID=notice'
        source = requests.get(url)
        source.encoding = None
        htmlSoup = BeautifulSoup(source.text, 'html.parser')

        for listCode in htmlSoup.find_all("tr", {"bgcolor": "#fffcdb"}):
            listSoup = BeautifulSoup(str(listCode), 'html.parser')

            # Extract Number
            url = listSoup.find('a')['href']
            url = str(url).replace("https://dormitory.cau.ac.kr/bbs/bbs_view.php?pNum=", "", 1)
            num = str(url).replace("&bbsID=notice", "", 1)
            self.IDNumbers.append((num))


            # Extract Title
            title = listSoup.find("span", {"class": "bbsTitle"})
            self.Titles.append(title.text)


            #Extract Date
            date = listSoup.find_all("td", {"class": "t_c"})[3]
            self.Dates.append(date.text)

def noticeNum(url):
    htmlSoup = BeautifulSoup(url, 'html.parser')
    number = htmlSoup.find_all("td", {"class": "v_t"})[0].text
    result = re.findall("\d\d\d\d", str(number))[0]
    return result

def noticeTitle(url):
    htmlSoup = BeautifulSoup(url, 'html.parser')
    title = htmlSoup.find_all("td", {"class": "bold f14"})[0].text
    result = str(title).replace("제목 : ", "", 1)
    print(result.encode('utf-8'))
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