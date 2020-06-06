# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:35:36 2020

@author: rowss
"""

import requests
from bs4 import BeautifulSoup


def get_price(ticker):
    stock = requests.get("https://finance.yahoo.com/quote/"+ticker)
    src = stock.content
    soup = BeautifulSoup(src, 'lxml')

    price= soup.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').span.text
    
    change = soup.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find_all('span')[1].text
    
    change = change.split(' ')
    real_change = change[0]
    change_percent = change[1]
    
    if real_change[0] == '+':
        print(f"{ticker} is {price}, up ${real_change} {change_percent} on the day")
    elif real_change[0] == '-':
        print(f"{ticker} is {price}, down ${real_change} {change_percent} on the day")
    else:
        print(f"{ticker} is {price}, with no change from the start of the day")
    
    return price



ticker = input("Enter the ticker of the stock you want to look up: ")
get_price(ticker)
