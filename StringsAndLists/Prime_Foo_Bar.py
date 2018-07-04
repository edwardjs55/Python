
pri = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
#pri = [1]
my_pri =[]
notprime= True
for i in range(2,30):
    if i% 2 == 0:
            break
    for j in pri:
        if i >= j:
            break
        if i % j == 0:
            break
    print i





    

    

