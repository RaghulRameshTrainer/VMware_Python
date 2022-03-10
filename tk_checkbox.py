from tkinter import *
import tkinter.messagebox as messagebox
root=Tk()
root.geometry("400x400")
chk1=IntVar()
chk2=IntVar()
chk3=IntVar()
def check():
    if chk1.get() == 1:
        messagebox.showinfo("Hello","You are from Chennai")
    elif chk2.get() == 1:
        messagebox.showinfo("Hello","You are from Bangalore")
    elif chk3.get() == 1:
        messagebox.showinfo("Hello","You are from Pune")
    else:
        pass
chkbtt1=Checkbutton(root,text="Chennai",variable=chk1,onvalue=1, offvalue=0,width=10,height=2)
chkbtt2=Checkbutton(root,text="Bangalore",variable=chk2,onvalue=1, offvalue=0,width=10,height=2)
chkbtt3=Checkbutton(root,text="Pune",variable=chk3,onvalue=1, offvalue=0,width=10,height=2)
btn=Button(root,text="Submit",command=check)

chkbtt1.pack()
chkbtt2.pack()
chkbtt3.pack()
btn.pack()
root.mainloop()