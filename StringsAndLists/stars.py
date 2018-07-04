def drawstars(list):
    string = ""
    for i in list:
        for j in range(0,i):
            string += "*"
        print string
        string = ""


def drawstars2(list):
    string = ""
    for i in list:
        if (type(i) is int):
            for j in range(0,i):
                string += "*"
            print string
            string = ""
        elif (type(i) is str):
            char = i[0].lower()
            for j in range(0,len(i)):
                string += char
            print string
            string = ""



x = ["Tom","Andy",5,7,3,"Philip"]
drawstars2(x)


print
print " first program: starsOnly"
drawstars([2,4,5,6,4,3,1])            
