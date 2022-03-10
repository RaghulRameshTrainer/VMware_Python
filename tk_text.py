from tkinter import *
import tkinter as tk
from tkinter import ttk
root=Tk()
root.title("Greeter")
root.geometry("400x400")

def myfunc():
    print(f"Hello {user_name.get() or 'RAGHUL' }, Thanks for attending the session")
n=ttk.Label(root,text="User Name:")
n.pack(side="left",padx=(0,0))
user_name=tk.StringVar()
x=ttk.Entry(root,textvariable=user_name)
x.pack(side="left")
x.focus()
btn=ttk.Button(root,text="Greet",command=myfunc)
btn.pack(side="right")
root.mainloop()