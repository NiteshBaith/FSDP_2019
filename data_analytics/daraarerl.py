# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:47:24 2019

@author: Baith
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://www.walmart.com"
driver = webdriver.Chrome("C:/Users/Baith/Chrome_driver/chromedriver.exe")

driver.get(url)

sleep(2)

bsk_input = driver.find_element_by_xpath('//*[@id="global-search-input"]')
inp=input("Enter input")
bsk_input.send_keys(inp)
search_result=driver.find_element_by_xpath('//*[@id="global-search-submit"]/span/span')

search_result.click()
sleep(5)

html_page = driver.page_source

soup = BS(html_page)

match=soup.find_all('div', class_='search-result-product-title gridview')
for row in data.:
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
           