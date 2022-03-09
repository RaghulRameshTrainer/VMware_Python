class Employee:
    #When we declare a variable inside a class, but outside the method, it is called a static or class variable.
    hike_percent = 5
    def __init__(self,fname,lname,pay=100):
        self.first_name=fname
        self.last_name=lname
        self.salary=pay
        self.email=self.first_name+"."+self.last_name+'@vmware.com'

    def mymethod(self):
        print("Hello How are you ")

    def __str__(self):
        str(input("x:"))
        return "This is the object for the Employee class"

    def __add__(self,other):
        return self.salary+other.salary

    def __raghul__(self):
        print("From dunder method")
    def fullname(self):
        return self.first_name+" "+self.last_name
    @classmethod
    def create_obj(cls,emp_info):
        cls.hike_percent
        cls.emp_info=emp_info
        fn,ln,sl=cls.emp_info.split("-")
        return cls(fn,ln,int(sl))    # Employee("Shivani","Kolanchi",100000)

    def appraisal(self):
        self.salary=int(self.salary*self.hike_percent)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

str1="Shivani-Kolanchi-100000"
str2="Harsha-Kolanchi-200000"

emp_1=Employee.create_obj(str1)
emp_2=Employee.create_obj(str2)

# print(Employee.hike_percent)
#
# import datetime
# my_date=datetime.date(2022,3,21)
#
# print(Employee.is_workingday(my_date))
#print(emp_1.salary)
#print(emp_2.salary)
#emp_1.hike_percent=5

#emp_1.appraisal()
#emp_2.appraisal()
#print("SALARY POST APPRAISAL CYCLE:")
#print(emp_1.salary)
#print(emp_2.salary)
#print(Employee.create_obj(str1))

# fn,ln,sl=str1.split("-")
# emp_1=Employee(fn,ln,sl)
# fn,ln,sl=str2.split("-")
# emp_2=Employee(fn,ln,sl)
#
# print(emp_1.email)
# print(emp_2.email)
#

class Developer(Employee):
    # def __init__(self,fname,lname,pay,tech):
    #     self.technology = tech
    #     super().__init__(fname,lname,pay)

    def callme(self):
        return self.fullname()

    def officelocation(self,country,state=""):
        self.country=country
        self.state=state
        if country=="India" and state=="Karnataka":
            print("Bangalore")
        else:
            print("Chennai")

    def fullname(self):
        return "{} {}".format(self.first_name.upper(), self.last_name.upper())

dev_1=Developer('Santosh','Krishan')
dev_2=Developer('Yogitha','Krishan')

print("{},{}".format(dev_1.email,dev_1.salary))
print("{},{}".format(dev_2.email,dev_2.salary))
#dev_1.officelocation("India","Karnataka")
print(dev_1.fullname())