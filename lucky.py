#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 03:11:10 2018
source : https://automatetheboringstuff.com/chapter11/
@author: nilesh
"""
# competitive programming
# lucky.py - Opens several Google search results.

import requests, webbrowser, bs4, pyperclip 

searchkey = pyperclip.paste()
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + searchkey) 
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))