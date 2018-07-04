class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal Health", self.health
        return self

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon !!!!"
        



# do some Testing/Calls
# 
Giraffe = Animal('giraffe',100)     
print Giraffe.name
Giraffe.displayHealth()
Giraffe.walk().walk().walk()
Giraffe.displayHealth()
Giraffe.run().run()
Giraffe.displayHealth()
print
Rascal = Dog('Rascal')
print Rascal.name
Rascal.displayHealth()
Rascal.walk().walk().walk()
Rascal.displayHealth()
Rascal.run().run()
Rascal.displayHealth()
Rascal.pet()
Rascal.displayHealth()

print
Iris = Dragon("Iris")
print Iris.name
Iris.displayHealth()
Iris.fly()
Iris.displayHealth()
# Rascal.fly()  ...has no such Attribute

lion = Animal('Tiger',200)
# lion.pet()   ...has no such Attribute
# lion.fly()   AttributeError: 'Animal' object has no attribute 'fly'


        
    