
def myfunct(x):
    if type(x) is int :
        print "I am an Integer : ",x
        if x > 100:
            print "Thats a big Number"
        else:
            print 'Thats a small number'            
    elif type(x) is str :
        print "I am a String: ",x
        if len(x) >= 50:
            print "Long Sentence"
        else:
            print "a Short Sentence"
    elif type(x) is list :
        print "IM A LIST, Yea for ME!!!", x
        if len(x) >= 10:
            print "A big, big List"
        else:
            print "That as small list"    
    else:
        print " I dont know what X is ???  ::",x

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

myfunct(sI)
myfunct(mI)
myfunct(bI)
myfunct(eI)
myfunct(spI)
myfunct(sS)
myfunct(mS)
myfunct(bS)
myfunct(eS)
myfunct(aL)
myfunct(mL)
myfunct(lL)
myfunct(eL)
myfunct(spL)

