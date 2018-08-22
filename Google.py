#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 03:30:26 2018

@author: nilesh
"""

import requests, webbrowser, bs4
from tkinter import *
from tkinter import messagebox

TOP = Tk()

TOP.geometry("400x400")
TOP.configure(background="#b0b7b6")
TOP.title("Google Search")
TOP.resizable(width=False, height=False)


def googlesearch():
    '''
       This function show the result
    '''
    searchkeyword = str(ENTRY1.get())
    messagebox.showinfo("Result", "Googling...")
    res = requests.get('http://google.com/search?q=' + searchkeyword) 
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    linkElems = soup.select('.r a')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))
 
large_font = ('Verdana',15)      
ENTRY1 = Entry(TOP, bd=2, width=20, font=large_font)
ENTRY1.place(x=65, y=90)
BUTTON = Button(bg="#53baf5", bd=12, text="Google Search", padx=33, pady=15, command=googlesearch,
                font=("Helvetica", 20, "bold"))
BUTTON.grid(row=3, column=0, sticky=W)
BUTTON.place(x=60, y=250)
TOP.mainloop()
