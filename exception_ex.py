'''
4 clauses in python exceptions
try
except
else
finally

'''


class MyOwnException(Exception):
    def ageError(self):
        pass

try:
    # with open("dayss.txt") as rf:
    #     print(rf.read())
    # x=int(input("Enter a number:"))
    # res=100/x
    # print("Result:",res)
    #2+"three"
    age=int(input("Enter your age:"))
    if age<0 or age>100:
        raise MyOwnException("Age cannot be less than 0 or greater than 100")
    print("Your age is : ",age)
except FileNotFoundError as e:
    print("File not found error received : ", e)
except PermissionError as e:
    print("Please check the file permission :",e)
except ZeroDivisionError as e:
    print("Can't divide by zero: ",e)
except MyOwnException as e:
    print("OWN EXCEPTION:",e)
except Exception as e:
    print("New Exception received by common exception block.", e)
else:
    print("NO EXCEPTION SEEMS!")
finally:
    print("FINALLY BLOCK!")
