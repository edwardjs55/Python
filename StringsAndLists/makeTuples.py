# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def showTuple(dict):
    newTuple = []
    newArr = ()
    for key,value in dict.iteritems():
        newArr = key, value
        newTuple.append(newArr)
        newArr = ()

    print
    print newTuple        

showTuple(my_dict)        




#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
