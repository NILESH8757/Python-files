#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 04:55:37 2018

@author: nilesh
"""

from tkinter import *
from tkinter import messagebox

TOP = Tk()

TOP.geometry("550x400")
TOP.configure(background="#C8AE96")
TOP.title("CF Score Calculator")
TOP.resizable(width=False, height=False)

def getmaxscore():
    '''
       This function gets the max score of 
       problems (A,B,C)
    '''
    score = [None] * 3
    score[0] = int(ENTRY11.get())
    score[1] = int(ENTRY12.get())
    score[2] = int(ENTRY13.get())
    
    return score 
    
def getrate():
    '''
       This function gets the point loss rate of each 
       problems (A,B,C)
    '''
    rate = [None] * 3
    rate[0] = int(ENTRY21.get())
    rate[1] = int(ENTRY22.get())
    rate[2] = int(ENTRY23.get())
    
    return rate
    
def getsubmissiontime():
    '''
       This function gets the submission time for 
       each problems (A,B,C)
    '''
    subtime = [None] * 3
    subtime[0] = int(ENTRY31.get())
    subtime[1] = int(ENTRY32.get())
    subtime[2] = int(ENTRY33.get())
    
    return subtime
    
def getpenality():
    '''
        This function gets no. of penalties (i.e., no. of
        WA/TLE/MLE/CE ) for each problems(A,B,C)
    '''  
    penality = [None] * 3
    penality[0] = int(ENTRY41.get())
    penality[1] = int(ENTRY42.get())
    penality[2] = int(ENTRY43.get())
    
    return penality
    
def calculatescore():
    '''
       This function calculates the total score & final score for each problems
       using given data
    '''
    try:
        score = getmaxscore()
        rate = getrate()
        subtime = getsubmissiontime()
        penality = getpenality()
        for sc in score:
            if sc < 500 or sc > 1500 :
                raise ValueError("Invalid Score! Try again.")
        for rt in rate:
            if rt <= 0 or rt > 10 :
                raise ValueError("Invalid Points Loss Rate! Try again.")
        for st in subtime:
            if st < 0 or st > 120 :
                raise ValueError("Invalid submission Time! Try again.")
        for pt in penality :
            if pt < 0 or pt > 100 :
                raise ValueError("Invalid no. of penality! Try again.")
    except ValueError as err:
        messagebox.showinfo("Result", err.args)
    except TypeError :
        messagebox.showinfo("Result", "Invalid Data!!")
    else:
        sa = score[0] - subtime[0] * rate[0] - penality[0] * 50
        sa = max(sa, 150)
        sb = score[1] - subtime[1] * rate[1] - penality[1] * 50
        sb = max(sb, 300)
        sc = score[2] - subtime[2] * rate[2] - penality[2] * 50
        sc = max(sc, 450)
        
        total = sa + sb + sc
        result = "A: "+str(sa) + "\nB: " + str(sb) + "\nC: " + str(sc) + "\nTotal: " + str(total)
        messagebox.showinfo("Score", result)
#first row widgets start here
LABLE1 = Label(TOP, bg="#d79983", text="Max. Score ->", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE1.place(x=20, y=30)
LABLE11 = Label(TOP, bg="#C8AE96", text="A:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE11.place(x=180, y=30)
ENTRY11 = Entry(TOP, bd=7, width=6)
ENTRY11.place(x=210, y=30)

LABLE12 = Label(TOP, bg="#C8AE96", text="B:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE12.place(x=290, y=30)
ENTRY12 = Entry(TOP, bd=7, width=6)
ENTRY12.place(x=320, y=30)

LABLE13 = Label(TOP, bg="#C8AE96", text="C:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE13.place(x=400, y=30)
ENTRY13 = Entry(TOP, bd=7, width=6)
ENTRY13.place(x=430, y=30)
#first row end here
#second row widgets start here
LABLE2 = Label(TOP, bg="#d79983", text="Points Loss/minute ->", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE2.place(x=20, y=80)
LABLE21 = Label(TOP, bg="#C8AE96", text="A:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE21.place(x=180, y=80)
ENTRY21 = Entry(TOP, bd=7, width=6)
ENTRY21.place(x=210, y=80)

LABLE22 = Label(TOP, bg="#C8AE96", text="B:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE22.place(x=290, y=80)
ENTRY22 = Entry(TOP, bd=7, width=6)
ENTRY22.place(x=320, y=80)

LABLE23 = Label(TOP, bg="#C8AE96", text="C:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE23.place(x=400, y=80)
ENTRY23 = Entry(TOP, bd=7, width=6)
ENTRY23.place(x=430, y=80)
#second row ends here

#third row widgets start here

LABLE3 = Label(TOP, bg="#d79983", text="Submission Time ->", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE3.place(x=20, y=130)
LABLE31 = Label(TOP, bg="#C8AE96", text="A:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE31.place(x=180, y=130)
ENTRY31 = Entry(TOP, bd=7, width=6)
ENTRY31.place(x=210, y=130)

LABLE32 = Label(TOP, bg="#C8AE96", text="B:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE32.place(x=290, y=130)
ENTRY32 = Entry(TOP, bd=7, width=6)
ENTRY32.place(x=320, y=130)

LABLE33 = Label(TOP, bg="#C8AE96", text="C:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE33.place(x=400, y=130)
ENTRY33 = Entry(TOP, bd=7, width=6)
ENTRY33.place(x=430, y=130)
#third row ends here
#fourth row widgets start here
LABLE4 = Label(TOP, bg="#d79983", text="No.of WA/TLE/MLE->", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE4.place(x=20, y=180)
LABLE41 = Label(TOP, bg="#C8AE96", text="A:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE41.place(x=180, y=180)
ENTRY41 = Entry(TOP, bd=7, width=6)
ENTRY41.place(x=210, y=180)

LABLE42 = Label(TOP, bg="#C8AE96", text="B:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE42.place(x=290, y=180)
ENTRY42 = Entry(TOP, bd=7, width=6)
ENTRY42.place(x=320, y=180)

LABLE43 = Label(TOP, bg="#C8AE96", text="C:", bd=8,
               font=("Helvetica", 10, "bold"))
LABLE43.place(x=400, y=180)
ENTRY43 = Entry(TOP, bd=7, width=6)
ENTRY43.place(x=430, y=180)
#fourth row ends here
#button start here
BUTTON = Button(bg="#1abaa2", bd=12, text="Score", padx=33, pady=15, command=calculatescore,
                font=("Helvetica", 20, "bold"))
BUTTON.grid(row=3, column=0, sticky=W)
BUTTON.place(x=180, y=300)
TOP.mainloop()