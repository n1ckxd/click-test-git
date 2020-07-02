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
def clear():
    global clicksgame
    global timegame
    global k
    mainbut.configure(text = "Начать тест")
    clicksgame = 0
    timegame = 0
    k = 1
    lblclicks['text'] = ("Клики:", clicksgame)
def timeplus():
    global k
    if k == 1:
        k = 0
        if timegame < 1:
            Timer = threading.Timer(10, timeplusser)
            Timer.start()
def timeplusser():
    global timegame
    lblclicks['text'] = ("Клики: 0")
    messagebox.showinfo('Время вышло!', ('Сделано кликов:', clicksgame))
    timegame = 1
    clear()
def click():
    global k
    global clicksgame
    global timegame
    timeplus()
    mainbut.configure(text = "Кликай!")
    if timegame < 1:
        clicksgame = clicksgame+1
        lblclicks['text'] = ("Клики:", clicksgame)   
lbltitle = Label(window, font = "Times 13", text = "Приветствую вас в моей программе!\nЗдесь вы сможете узнать,сколько кликов вы сможете сделать за 10 секунд.")
lblspace = Label(window, text = "", bg = "white")
lblclicks = Label(window, font = "Times 18", text = ("Клики:", clicksgame))
mainbut = Button(window, width=70, height=20, bd = "3", text = "Начать тест", command=click)
lbltitle.pack()
lblspace.pack()
mainbut.pack()
lblclicks.pack()
window.mainloop()
