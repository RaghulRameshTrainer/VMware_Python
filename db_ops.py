import sqlite3

dbh=sqlite3.connect("vmware.db")
c=dbh.cursor()

def create_table():
    c.execute("""CREATE TABLE employee(empid TEXT,name TEXT,tech TEXT)""")

def insert_data():
    eid=int(input("Emp ID:"))
    ename=input("Emp Name:")
    etech=input("Tech:")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(eid,ename,etech))

def delete_record():
    c.execute("DELETE  FROM employee WHERE tech='Mainframe'")

def update_records():
    c.execute("UPDATE employee SET tech='Python' WHERE tech in ('Java','DevOps')")

def fetch_records():
    c.execute("SELECT * FROM employee")
    ####fechone, fetchmany,fetchall
    #print(c.fetchone())
    #print(c.fetchmany(5))
    # for r in c.fetchall():
    #     print("{} ====> {}".format(r[1],r[2]))
    print(c.fetchall()[:3])
#create_table()
# for x in range(5):
#     insert_data()
#delete_record()
#update_records()
fetch_records()
dbh.commit()
c.close()
dbh.close()

