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
colosec = 0
colshssec = 0
timemain = "tsec"
def colosecplus():
    global timemain
    global coltsec
    global coltrsec
    global colfsec
    global colshssec
    if colosec%2 != 0:
        osecbut.configure(bg = "gray")
        if coltsec%2 !=0:
            coltsec = 2
            tsecbut.configure(bg = "white")
        if colfsec%2 !=0:
            colfsec = 2
            fsecbut.configure(bg = "white")
        if coltrsec%2 !=0:
            coltrsec = 2
            trsecbut.configure(bg = "white")
        if colshssec%2 !=0:
            colshssec = 2
            shssecbut.configure(bg = "white")
    else:
        osecbut.configure(bg = "white")
        timemain = "tsec"
def colfsecplus():
    global timemain
    global coltsec
    global coltrsec
    global colosec
    global colshssec
    if colfsec%2 != 0:
        fsecbut.configure(bg = "gray")
        if coltsec%2 !=0:
            coltsec = 2
            tsecbut.configure(bg = "white")
        if colosec%2 !=0:
            colosec = 2
            osecbut.configure(bg = "white")
        if coltrsec%2 !=0:
            coltrsec = 2
            trsecbut.configure(bg = "white")
        if colshssec%2 !=0:
            colshssec = 2
            shssecbut.configure(bg = "white")
    else:
        fsecbut.configure(bg = "white")
        timemain = "tsec"
def coltsecplus():
    global timemain
    global colfsec
    global coltrsec
    global colosec
    global colshssec
    if coltsec%2 != 0:
        tsecbut.configure(bg = "gray")
        if colfsec%2 !=0:
            colfsec = 2
            fsecbut.configure(bg = "white")
        if colosec%2 !=0:
            colosec = 2
            osecbut.configure(bg = "white")
        if coltrsec%2 !=0:
            coltrsec = 2
            trsecbut.configure(bg = "white")
        if colshssec%2 !=0:
            colshssec = 2
            shssecbut.configure(bg = "white")
    else:
        tsecbut.configure(bg = "white")
        timemain = "tsec"
def coltrsecplus():
    global timemain
    global colfsec
    global coltsec
    global colosec
    global colshssec
    if coltrsec%2 != 0:
        trsecbut.configure(bg = "gray")
        if colfsec%2 !=0:
            colfsec = 2
            fsecbut.configure(bg = "white")
        if colosec%2 !=0:
            colosec = 2
            osecbut.configure(bg = "white")
        if coltsec%2 !=0:
            coltsec = 2
            tsecbut.configure(bg = "white")
        if colshssec%2 !=0:
            colshssec = 2
            shssecbut.configure(bg = "white")
    else:
        trsecbut.configure(bg = "white")
        timemain = "tsec"
def colshssecplus():
    global timemain
    global colfsec
    global coltsec
    global colosec
    global coltrsec
    if colshssec%2 != 0:
        shssecbut.configure(bg = "gray")
        if colfsec%2 !=0:
            colfsec = 2
            fsecbut.configure(bg = "white")
        if colosec%2 !=0:
            colosec = 2
            osecbut.configure(bg = "white")
        if coltsec%2 !=0:
            coltsec = 2
            tsecbut.configure(bg = "white")
        if coltrsec%2 !=0:
            coltrsec = 2
            trsecbut.configure(bg = "white")
    else:
        shssecbut.configure(bg = "white")
        timemain = "tsec"
def osec():
    global timemain
    global colosec
    timemain = "osec"
    colosec = colosec + 1
    colosecplus()
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
def shssec():
    global timemain
    global colshssec
    timemain = "shssec"
    colshssec = colshssec + 1
    colshssecplus()
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
    osecbut.pack()
    fsecbut.pack()
    tsecbut.pack()
    trsecbut.pack()
    shssecbut.pack()
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
def timeplusosec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(1, timeplusserosec)
            Timer.start()
def timeplus30sec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(30, timeplusser30sec)
            Timer.start()
def timeplusshssec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(60, timeplussershssec)
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
def timeplusserosec():
    global timegame
    global crntclicks
    lblclicks['text'] = ("Клики: 0")
    clicksgamenum = float(clicksgame)
    crntclicks = (clicksgamenum / 1)
    if str(crntclicks).endswith('.0'):
        crntclicks = str(crntclicks)[:-2]
    if str(crntclicks).endswith('1'):
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} клик в секунду.'.format(clicksgame, crntclicks))
    else:
        messagebox.showinfo('Время вышло!', 'Сделано кликов: {}.\nВ среднем вы делаете {} кликов в секунду.'.format(clicksgame, crntclicks))
    timegame = 1
    clear()
def timeplussershssec():
    global timegame
    global crntclicks
    lblclicks['text'] = ("Клики: 0")
    clicksgamenum = float(clicksgame)
    crntclicks = (clicksgamenum / 60)
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
    osecbut.pack_forget()
    shssecbut.pack_forget()
    
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
    if timemain == "osec":
        timeplusosec()
        mainbut.configure(text = "Кликай!")
        if timegame < 1:
            clicksgame = clicksgame+1
            lblclicks['text'] = ("Клики:", clicksgame)
    if timemain == "shssec":
        timeplusshssec()
        mainbut.configure(text = "Кликай!")
        if timegame < 1:
            clicksgame = clicksgame+1
            lblclicks['text'] = ("Клики:", clicksgame)
lbltitle = Label(window, font = "Times 13", text = "Приветствую вас в моей программе!\nЗдесь вы сможете узнать,сколько кликов вы сможете сделать за 1/5/10/30/60 секунд.\nПо умолчанию тест идёт на 10 секунд.\nДля того,чтобы увидеть все кнопки разверните окно.")
lblspace = Label(window, text = "", bg = "white")
lblclicks = Label(window, font = "Times 18", text = ("Клики:", clicksgame))
mainbut = Button(window, width=70, height=20, bd = "3", bg = "#4869D6", activebackground="#FF8C00", text = "Начать тест", command=click)
osecbut = Button(window, width=10, height=3, bd = "3", bg = "white", activebackground="gray", text = "1 секунда", command=osec)
fsecbut = Button(window, width=10, height=3, bd = "3", bg = "white", activebackground="gray", text = "5 секунд", command=fsec)
tsecbut = Button(window, width=10, height=3, bd = "3", bg = "white", activebackground="gray", text = "10 секунд", command=tsec)
trsecbut = Button(window, width=10, height=3, bd = "3", bg = "white", activebackground="gray", text = "30 секунд", command=trsec)
shssecbut = Button(window, width=10, height=3, bd = "3", bg = "white", activebackground="gray", text = "60 секунд", command=shssec)
mainbut.bind("<Enter>", on_enter)
mainbut.bind("<Leave>", on_leave)
lbltitle.pack()
lblspace.pack()
mainbut.pack()
lblclicks.pack()
osecbut.pack()
fsecbut.pack()
tsecbut.pack()
trsecbut.pack()
shssecbut.pack()
window.mainloop()
input()
