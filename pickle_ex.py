import pickle

mylist=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

with open("proj.txt","wb") as fh:
    pickle.dump(mylist,fh)
