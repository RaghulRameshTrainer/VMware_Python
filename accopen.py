from oops_ec import User

myacc=User("Raghul","Raghul@gmail.com","9884811111",10000)
print("Username : {} and Password: {} and Balance: {}".
      format(myacc.user,myacc.password,myacc.getbalance()))

#myacc.setbalance(90000)
myacc._User__balance=10000000
print("My account balance: {}".format(myacc.getbalance()))

