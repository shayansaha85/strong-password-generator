from tkinter import *
import string as s
from random import *
import os

root = Tk()
root.geometry("400x300")
root.title("Password generator - By Shayan")

photo = PhotoImage(file = ".img\\891399.png")
root.iconphoto(False, photo)

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    filename = inputtxt2.get("1.0", "end-1c")
    length = int(INPUT)
    password = ""
    i = 0
    ch = s.ascii_letters + s.digits + s.punctuation
    while i<length:
        password += ch[randint(1,len(ch)-1)]
        i=i+1
    if "passwords" not in os.listdir():
        os.mkdir("passwords")
    file = open(f"passwords\\{filename}.txt", "w")
    file.write(password)
    file.close()
      
l = Label(text = "Enter length of password (e.g. 23)")
inputtxt = Text(root, height=2, width=40)

l2 = Label(text = "Enter one filename (e.g. webmailPass)")
inputtxt2 = Text(root, height=2, width=40)

l3 = Label(text = "")
l4 = Label(text = "")
l5 = Label(text = "")

Display = Button(root, height = 2,
                 width = 20, 
                 text ="Generate Password",
                 command = lambda:Take_input())

l5.pack()
l.pack()
inputtxt.pack()
l3.pack()
l2.pack()
inputtxt2.pack()
l4.pack()
Display.pack()
root.mainloop()