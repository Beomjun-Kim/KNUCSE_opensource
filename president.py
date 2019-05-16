#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

	url = "https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States"
	res = requests.get(url)
	soup = BeautifulSoup(res.content,'html.parser')
	tb = soup.find('table',class_='wikitable')

	for link in tb.find_all('b'):
			name=link.find('a')
			print(name)
	
	for link in tb.find_all('b'):
			name = link.find('a')
			print(name.get_text('title'))
