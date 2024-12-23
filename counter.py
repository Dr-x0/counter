from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root=Tk()
root.geometry("300x200")
root.title("counter")
h=0
def loop():
    global h
    h+=1
    Label(root,text=h,bg="#F5E216").place(x=120,y=5) 


     
   

        
        

         
        

#n=tk.StringVar()
#monthchoosen = ttk.Combobox(root, width = 15,cursor="hand1")
# Adding combobox drop down list 
#monthchoosen['values'] = ('sobhan allh',
#                          'alhamdw llah',
#                           'la alah ela allh',
#                            'astgfer allh' )      

Button(root,
       text="click",
       command=loop,
       width=15,
       height=10,
       bg="#FFA62F",
       activebackground="#F5E216",
       activeforeground="#FFA500",
       cursor="hand1").place(x=120,y=30)

#monthchoosen.grid(column = 9, row = 9) 
#monthchoosen.current() 
root.mainloop()
#
