from tkinter import *  #Tk
root=Tk()

def clickme():
    l=Label(root,text="Welcome to Python World",font=("Arial",50))
    l.pack()
root.geometry('1000x400')  #width x height
# l=Label(root,text="VMWARE",font=("Arial",20),bg="red",fg="white",width=200,height=2)
# l.pack()
#Create a button
b=Button(root,text="Click Me",bg="yellow",fg="blue",font=("Arial",20),command=clickme,
         activebackground="blue",activeforeground="red", highlightbackground="black",
         highlightthickness=10)
b.pack()
root.mainloop()




