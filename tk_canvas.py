from tkinter import *

root=Tk()
c=Canvas(root,width=600,height=500)
c.create_line(0,0,600,500,width=3,fill="red",dash=(3,3))
c.create_line(0,500,600,0,width=3,fill="red",dash=(3,3))
c.create_rectangle(150,125,450,375,fill="yellow",outline="blue",width=2)
c.create_oval(100,100,300,300,width=3,fill="green")
c.create_arc(100,100,300,300,width=3,fill="green",start=90,extent=270)
c.pack()
root.mainloop()