#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

	ch = raw_input("input sign > ")

	url = "https://www.nasdaq.com/symbol/"+ch
	res = requests.get(url)
	soup = BeautifulSoup(res.content,'html.parser')
	
	price = soup.find(id="qwidget_lastsale")
	change = soup.find(id="qwidget_netchange")
	percent = soup.find(id="qwidget_percent")

	print "price : ",
	print price.text
	print "changed amount : ",
	print change.text
	print "percent : ",
	print percent.text
