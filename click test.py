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
def on_enter(e):
    mainbut['background'] = '#06266F'
def on_leave(e):
    mainbut['background'] = '#4869D6'
def clear():
    global clicksgame
    global timegame
    global k
    mainbut.configure(text = "Начать тест")
    clicksgame = 0
    timegame = 0
    k = 1
    lblclicks['text'] = ("Клики:", clicksgame)
def timeplus10sec():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(10, timeplusser10sec)
            Timer.start()
def timeplusser10sec():
    global timegame
    global crntclicks
    lblclicks['text'] = ("Клики: 0")
    clicksgamenum = float(clicksgame)
    crntclicks = (clicksgamenum / 10)
    if str(crntclicks).endswith('1'):
        messagebox.showinfo('Время вышло!', ('Сделано кликов:', clicksgame, "\nВ среденем вы делаете", crntclicks, "клик в секунду."))
    else:
        messagebox.showinfo('Время вышло!', ('Сделано кликов:', clicksgame, "\nВ среденем вы делаете", crntclicks, "кликов в секунду."))
    timegame = 1
    clear()
def click():
    global k
    global clicksgame
    global timegame
    timeplus10sec()
    mainbut.configure(text = "Кликай!")
    if timegame < 1:
        clicksgame = clicksgame+1
        lblclicks['text'] = ("Клики:", clicksgame)   
lbltitle = Label(window, font = "Times 13", text = "Приветствую вас в моей программе!\nЗдесь вы сможете узнать,сколько кликов вы сможете сделать за 10 секунд.")
lblspace = Label(window, text = "", bg = "white")
lblclicks = Label(window, font = "Times 18", text = ("Клики:", clicksgame))
mainbut = Button(window, width=70, height=20, bd = "3", bg = "#4869D6", activebackground="#FF8C00", text = "Начать тест", command=click)
mainbut.bind("<Enter>", on_enter)
mainbut.bind("<Leave>", on_leave)
lbltitle.pack()
lblspace.pack()
mainbut.pack()
lblclicks.pack()
window.mainloop()
