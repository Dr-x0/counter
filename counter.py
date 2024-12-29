from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time

root = Tk()
root.geometry("300x250")
root.title("counter")
h = 0

def loop():
    global h
    h += 1
    Label(root, text=h, bg="#F5E216").place(x=120, y=5) 

def reset():
    global h
    h = 0
    Label(root, text=h, bg="#F5E216").place(x=120, y=5)

def show_time():
    current_time = time.strftime('%H:%M:%S')
    Label(root, text=current_time, bg="#F5E216").place(x=120, y=50)

Button(root, text="click", command=loop, width=15, height=2, bg="#FFA62F", activebackground="#F5E216", activeforeground="#FFA500", cursor="hand1").place(x=120, y=80)
Button(root, text="reset", command=reset, width=15, height=2, bg="#FF6347", activebackground="#F5E216", activeforeground="#FFA500", cursor="hand1").place(x=120, y=130)
Button(root, text="Show Time", command=show_time, width=15, height=2, bg="#32CD32", activebackground="#F5E216", activeforeground="#FFA500", cursor="hand1").place(x=120, y=180)

root.mainloop()
