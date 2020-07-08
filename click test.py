import threading
import time
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title ("Click test")
window.geometry("600x600")
window["bg"] = "white"
clicksgame = 0
timegame = 0
k = 1
crntclicks = 0
clicksgamenum = 0
colfsec = 0
coltsec = 0
coltrsec = 0
timemain = "tsec"
def colfsecplus():
    global timemain
    global coltsec
    global coltrsec
    if colfsec%2 != 0:
        fsecbut.configure(bg = "gray")
        if coltsec%2 !=0:
            coltsec = 2
            tsecbut.configure(bg = "white")
        if coltrsec%2 !=0:
            coltrsec = 2
            trsecbut.configure(bg = "white")
    else:
        fsecbut.configure(bg = "white")
        timemain = "tsec"
def coltsecplus():
    global timemain
    global colfsec
    global coltrsec
    if coltsec%2 != 0:
        tsecbut.configure(bg = "gray")
        if colfsec%2 !=0:
            colfsec = 2
            fsecbut.configure(bg = "white")
        if coltrsec%2 !=0:
            coltrsec = 2
            trsecbut.configure(bg = "white")
    else:
        tsecbut.configure(bg = "white")
        timemain = "tsec"
def coltrsecplus():
    global timemain
    global colfsec
    global coltsec
    if coltrsec%2 != 0:
        trsecbut.configure(bg = "gray")
        if colfsec%2 !=0:
            colfsec = 2
            fsecbut.configure(bg = "white")
        if coltsec%2 !=0:
            coltsec = 2
            tsecbut.configure(bg = "white")
    else:
        trsecbut.configure(bg = "white")
        timemain = "tsec"
def fsec():
    global timemain
    global colfsec
    timemain = "fsec"
    colfsec = colfsec + 1
    colfsecplus()
def tsec():
    global timemain
    global coltsec
    timemain = "tsec"
    coltsec = coltsec + 1
    coltsecplus()
def trsec():
    global timemain
    global coltrsec
    timemain = "trsec"
    coltrsec = coltrsec + 1
    coltrsecplus()
def on_enter(e):
    mainbut['background'] = '#06266F'
def on_leave(e):
    mainbut['background'] = '#4869D6'
def clear():
    global clicksgame
    global timegame
    global k
    global clicksgamenum
    global crntclicks
    mainbut.configure(text = "Начать тест")
    clicksgame = 0
    timegame = 0
    k = 1
    lblclicks['text'] = ("Клики:", clicksgame)
    clicksgamenum = 0
    crntclicks = 0
    fsecbut.pack()
    tsecbut.pack()
    trsecbut.pack()
def timeplus10sec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(10, timeplusser10sec)
            Timer.start()
def timeplus5sec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(5, timeplusser5sec)
            Timer.start()
def timeplus30sec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(30, timeplusser30sec)
            Timer.start()
def timeplusser10sec():
    global timegame
    global crntclicks
    lblclicks['text'] = ("Клики: 0")
    clicksgamenum = float(clicksgame)
    crntclicks = (clicksgamenum / 10)
    if str(crntclicks).endswith('.0'):
        crntclicks = str(crntclicks)[:-2]
    if str(crntclicks).endswith('1'):
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} клик в секунду.'.format(clicksgame, crntclicks))
    else:
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} кликов в секунду.'.format(clicksgame, crntclicks))
    timegame = 1
    clear()
def timeplusser5sec():
    global timegame
    global crntclicks
    lblclicks['text'] = ("Клики: 0")
    clicksgamenum = float(clicksgame)
    crntclicks = (clicksgamenum / 5)
    if str(crntclicks).endswith('.0'):
        crntclicks = str(crntclicks)[:-2]
    if str(crntclicks).endswith('1'):
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} клик в секунду.'.format(clicksgame, crntclicks))
    else:
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} кликов в секунду.'.format(clicksgame, crntclicks))
    timegame = 1
    clear()
def timeplusser30sec():
    global timegame
    global crntclicks
    lblclicks['text'] = ("Клики: 0")
    clicksgamenum = float(clicksgame)
    crntclicks = (clicksgamenum / 30)
    if str(crntclicks).endswith('.0'):
        crntclicks = str(crntclicks)[:-2]
    if str(crntclicks).endswith('1'):
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} клик в секунду.'.format(clicksgame, crntclicks))
    else:
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} кликов в секунду.'.format(clicksgame, crntclicks))
    timegame = 1
    clear()
def click():
    tsecbut.pack_forget()
    fsecbut.pack_forget()
    trsecbut.pack_forget()
    global k
    global clicksgame
    global timegame
    if timemain == "tsec":
        timeplus10sec()
        mainbut.configure(text = "Кликай!")
        if timegame < 1:
            clicksgame = clicksgame+1
            lblclicks['text'] = ("Клики:", clicksgame)
    if timemain == "fsec":
        timeplus5sec()
        mainbut.configure(text = "Кликай!")
        if timegame < 1:
            clicksgame = clicksgame+1
            lblclicks['text'] = ("Клики:", clicksgame)
    if timemain == "trsec":
        timeplus30sec()
        mainbut.configure(text = "Кликай!")
        if timegame < 1:
            clicksgame = clicksgame+1
            lblclicks['text'] = ("Клики:", clicksgame)
lbltitle = Label(window, font = "Times 13", text = "Приветствую вас в моей программе!\nЗдесь вы сможете узнать,сколько кликов вы сможете сделать за 10 или 5 секунд.\nПо умолчанию тест идёт на 10 секунд.")
lblspace = Label(window, text = "", bg = "white")
lblclicks = Label(window, font = "Times 18", text = ("Клики:", clicksgame))
mainbut = Button(window, width=70, height=20, bd = "3", bg = "#4869D6", activebackground="#FF8C00", text = "Начать тест", command=click)
fsecbut = Button(window, width=10, height=5, bd = "3", bg = "white", activebackground="gray", text = "5 секунд", command=fsec)
tsecbut = Button(window, width=10, height=5, bd = "3", bg = "white", activebackground="gray", text = "10 секунд", command=tsec)
trsecbut = Button(window, width=10, height=5, bd = "3", bg = "white", activebackground="gray", text = "30 секунд", command=trsec)
mainbut.bind("<Enter>", on_enter)
mainbut.bind("<Leave>", on_leave)
lbltitle.pack()
lblspace.pack()
mainbut.pack()
lblclicks.pack()
fsecbut.pack()
tsecbut.pack()
trsecbut.pack()
window.mainloop()
input()
