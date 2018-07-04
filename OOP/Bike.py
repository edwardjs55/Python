class Bike(object):
    def __init__(self,price,speed):
        self.price = price
        self.max_speed = speed
        self.miles = 0

    def displayInfo(self):
        print "Bike Price: $",self.price," Max Speed: ",self.max_speed," Miles: ",self.miles
        return self

    def ride(self):
        self.miles += 10
        print "Riding is a Breeze.."
        return self

    def reverse(self):
        self.miles -= 5
        print "Bamm..In Reverse.."
        return self




myBike = Bike(250,"100mph")
yourBike = Bike(10,"10mph")
MikesBike = Bike(300,"300mph")

myBike.ride()
myBike.ride()
myBike.ride()
myBike.reverse()
myBike.displayInfo()

yourBike.ride().ride().reverse().reverse().displayInfo()

MikesBike.reverse().reverse().reverse().displayInfo()

# prevent Negatives miles by coding logic in Reverse Method
# All methods should return self Or else it will return null by default
# which will alsso prevent chaining...







