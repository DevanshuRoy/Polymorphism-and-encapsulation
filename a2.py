class Computer:

    def __init__(self,a,b):
        # private is not accessible outside class
        self.__maxprice=a #private datamember
        self.price=b

    def sell(self):
        print("Selling Price: ",self.__maxprice)
        print("Actual Price: ",self.price)

    def setMaxPrice(self):
        self.__maxprice = self.__maxprice+(20*self.__maxprice/100)

c = Computer(1000,800)
c.sell()

# change the price
c.__maxprice = 2000 #maxprice doesnt change
c.price=1000 #price changes
c.sell()

# using setter function
c.setMaxPrice()
c.sell()