class Car(object):
    def __init__(self,price,speed,fuel,miles):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.miles = miles
        self.tax = 0.12
        if(self.price > 10000 ): self.tax = 0.15
        self.display_all()

    def display_all(self):
        print
        print "Price:  $" , self.price
        print "Speed:   "  , self.speed
        print "Fuel :   "  , self.fuel
        print "Mileage: " , self.miles
        print "Tax:     ", self.tax
        print
        return self

firebird = Car(18000,"180 mph","18 g",500)
volswagon = Car(200,"55 mph","200mpg",500000)
ModelT = Car(45,"40 mph","10mpg",100000)
alphaR = Car(21000,"140mph","40mpg",10)
Cadillac = Car(38000,"145mph","33mpg",2)
Fiat = Car(29000,"120mph","35mpg",15000)


