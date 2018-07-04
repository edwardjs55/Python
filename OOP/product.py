class Product(object):
    def __init__(self,item,brand,price,weight):
        self.itemName = item
        self.brand = brand
        self.price = price
        self.weight = weight
        self.status = "for sale"

    def sell(self):
        self.status = 'sold'
        return self

    def addTax(self,tax):
        self.price = self.price *(1+tax)
        return self.price

    def Return(self,reason):
        if(reason == "defective"):
            self.status = reason
            self.price = 0
        if(reason == "in the box"):
            self.status = "for sale"
        if(reason == "opened"):
            self.status = "used"
            self.price *=(.80)
        return self

    def displayInfo(self):
        print
        print "Item:", self.itemName
        print "Brand:", self.brand
        print "Price:", self.price
        print "Weight:", self.weight
        print "Status:", self.status
        return self

shoes = Product("Shoes","Gucci",200,3.5)

print "Display"
shoes.displayInfo()
print "Sold"
shoes.sell()
print " Info"
shoes.displayInfo()
print "Returned as opened ~ discounted"
shoes.Return('opened')
shoes.displayInfo()
print "Add tax"
shoes.addTax(0.0825)
shoes.displayInfo()








        
