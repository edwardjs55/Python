
def listJob(arr):
    sum = 0
    string = ""
    msg = ""
    for i in arr:
        # print i, type(i)
        if type(i) is int:
            sum = sum + i
        if type(i) is str:
            # print "build the string" 
            string = string + i

    if(string == '' and sum > 0):
        msg = "All integers today !!!"
        print msg
        print "Sum = ",sum,string
        return

    elif(sum == 0 and string != ""):
        msg = "All strings today!!"
        print msg
        print "String= ",string
        return
    else: 
        msg =" A nice mix of Integers and String"
        print msg
        print "Sum = ",sum
        print "String= ",string


listJob(["I dont like Lobster",3,4,567,8,9])   
