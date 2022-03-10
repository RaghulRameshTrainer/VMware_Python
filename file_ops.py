'''
mode:
r (read,optional) -> default mode. if the file is not there we will get FileNotFoundError.
w (write) -> if the file is not there then it will create the file and start writing into it
             if the file is there it will remove the existing content and start writing as a new file.
a(appned) -> if the file is not there then it will create the file and start writing into it
            if the file is there it will start appending to the existing file content
r+( read and write) -> file will get opened for read and write .
w+ (write and read) -> cleanup the existing content , we will write and we will read whatever has
                        been written
rb (read binary) ->
wb (write binary) ->
'''

with open("days.txt","r") as rf:
    #readline, readlines, read
    print(rf.readline(),end="")
    # for day in rf.readlines()[4:]:
    #     print(day,end='')
    print(rf.read())
    rf.seek(0,0)
    print("====>",rf.read())


#with open("attendance.txt","w") as wfh:
    #write, writelines
    #wfh.write("Ajitabh")
    #wfh.writelines(["Ajitabh\n","Balaji\n","Archana\n"])
    #wfh.writelines(['Ramachandran\n',"Chandrasekar"])

# with open("attendance.txt",'a') as af:
#     af.writelines(['Ramachandran\n',"Chandrasekar"])

# with open("attendance.txt","w") as wfo:
#     wfo.writelines(['India\n'])
#     wfo.writelines("USA\n")
#     wfo.writelines("Singapore\n")
#     wfo.writelines("Canada\n")
#     wfo.writelines("Australia\n")
#     wfo.writelines("China")
#
# fo=open("attendance.txt","w")
# fo.writelines("VMWare\n")
# fo.writelines("India\n")
# print("I am done with file")
# print("Thanks all")
# fo.writelines("Python")
# fo.close()
# fo.writelines("Java")
# print(fo.closed)
#
#
# with open("attendance.txt","r+") as fo:
#     #print("The existing file contents are follows:")
#     #print(fo.read())
#     fo.writelines(["GREEN\n","BLUE\n","RED\n","WHITE\n","YELLOW"])
#
# with open("attendance.txt","w+") as fo:
#     fo.writelines(["Python\n","Java\n","AIML"])
#     fo.seek(0,0)
#     print("Current cursor position:",fo.tell())
#     print("File contents are:\n",fo.read())
#
#
# with open(r"D:\Users\rkandasamy\Pictures\puppy.jpg","rb") as fo:
#     with open(r"D:\Users\rkandasamy\Pictures\puppy_copied.jpg","wb") as wo:
#         wo.writelines(fo.readlines())
