from abc import ABC,abstractmethod
class Car(ABC):   #Abstract BaseClass
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def wheels(self):
        pass
    @abstractmethod
    def stearing(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def mirror(self):
        pass

    def seats(self):
        return "8+1 seater"

class EcoSport(Car):
    def __init__(self,make,model,model_year):
        self.make=make
        self.model=model
        self.my=model_year
    def breaks(self):
        self.applied=True
    def wheels(self):
        self.count=5
    def stearing(self):
         self.fitted=True
    def engine(self):
        self.engine_type="Powerstain"
    def mirror(self):
        self.count=5
    def price(self):
        return 1300000

es1=EcoSport("Ford","ES",2022)
print("Car Price:",es1.price())
print("Seats Capacity:",es1.seats())

