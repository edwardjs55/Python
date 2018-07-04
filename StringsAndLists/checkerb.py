white = "*"
black = " "
string= ""
for j in range(1,65):
    if(j%2 ==1):
        string += white
    else:
        string += black
    #print j    
    if(j%8 == 0):        
        print string
        string = ''
        temp = white
        white = black
        black = temp

    