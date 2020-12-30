#client


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


import socket
import time
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
LEFT = 1
SCROLL = 2
RIGHT = 3
red = (255,0,0)
reder = (230,0,0)
green = (0,200,0)
blue = (0,0,250)
black = (0,0,0)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


IP = "127.0.0.1"
PORT = 42069


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


def helloCallBack():
    messagebox.showinfo("Hello", "Hi there")


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


root = Tk()
root.title("poker")
root.iconbitmap('chip.ico')
file = "Poker_startpage.png"
def main():
    bg = Canvas(root, bg="white", height = 451, width = 906)
    bg.pack()
    start_image = PhotoImage(file = "Poker_startpage.png")
    bg.create_image(455, 230, image=start_image)
    btn1 = Button(root, text='Enter' ,fg="black",activebackground = "green",width = 28, height = 5, activeforeground = "black",bg = "red", relief=FLAT,command = helloCallBack, font = ( 150))
    btn1 = bg.create_window(365,320,anchor='nw', window=btn1)
    #btn1.place(x=0,y=0)

    root.mainloop()








if __name__ == '__main__':
    main()
