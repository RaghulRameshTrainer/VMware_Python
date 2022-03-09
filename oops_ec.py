class User:
    def __init__(self,name,email,mobile,deposit):
        self.name=name
        self.mobile=mobile
        self.user=email
        self.__balance=deposit
        self.password="abc123"

    def setbalance(self,amount):
        self.__balance=self.__balance+amount

    def getbalance(self):
        return self.__balance