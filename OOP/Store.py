class Store(object):
    def __init__(self,owner,location):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self,product): # Add product to Store's products Array
        self.products.append(product)
        return True

    def add_products(self,*products): # Add product to Store's products Array
        for product in products:
            self.products.append(product)
        return True

    def remove_product(self,product): # Remove product from Store's products Array
        self.products.remove(product)
        return True

    def inventory(self): # print store product info
        # for product in self.products:
        for product in self.products:
            product.displayInfo()

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
        print "Item:", self.itemName,
        print " Brand:", self.brand,
        print " Price:", self.price,
        print " Weight:", self.weight,
        print " Status:", self.status,
        return self

shoes = Product("Shoes","Gucci",200,3.5)
shirt = Product('Shirt','WalMart',15,2)
pants = Product('Blue jeans','Levis',33,3)
print "Display"
shoes.displayInfo()
print
Nikos = Store('Gabby Nikos','121 main st, Dallas,TX')
print 'Store Info: ',Nikos.owner,Nikos.location

Nikos.add_product(shoes)
Nikos.add_products(shirt,pants)
print
print 'Inventory:',
Nikos.inventory()
