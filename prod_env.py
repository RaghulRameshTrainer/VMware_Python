import pickle

with open("proj.txt","rb") as fo:
    days=pickle.load(fo)
    print(days)

