def compareLists(x,y):
    if x == y:
        print " X and Y are Equal"
    else:
        print "List X and Y ar NOT equal"

x= [1,2,3,45,6]        
y= [1,2,3,45,6,"rex"]

compareLists(x,y)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
list_three = ['celery','carrots','bread','cream']

compareLists(list_one,list_two)
compareLists(list_three,list_two)