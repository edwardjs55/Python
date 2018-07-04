
#Dictionaries : create & Read

#create Dictionary
myDict = {"name": "Edward Solo", "age": "25","country":"USA", "fav_lang": "python","fav_food": "Mexican","fav_movie": "Jabberwocky" }

def printDict(dict):
    for key,data in dict.iteritems():
        print key," = ",data


print 
print "my Dictionary Information"
printDict(myDict)