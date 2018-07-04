def oddEven():
    for i in range(1,200):
        if(i % 2 == 1):
            print "Number is ",i,". This is an odd Number."
        else:
            print "Number is ",i,". This is an even Number."



def multiply(arr,x):
    newArr = []
    z = 0
    for i in arr:
        z = i * x
        newArr.append(z)
    print " New Array: ", newArr
    return newArr

def layerdMultis(arrM):
    newArr = []
    outArr = []
    for a in range(0,len(arrM)):   # a is a Number from the Array
        for b in range(0,arrM[a]):
            newArr.append(1)
            
        outArr.append(newArr)
        newArr = []
    # print outArr            
    return outArr




q = [5,6,7,8,9,12]
v = [1,2,3]
p = layerdMultis(multiply(v,5))
print p



q = [5,6,7,8,9,12]
multiply(q,5)


#output / Function calls

oddEven()