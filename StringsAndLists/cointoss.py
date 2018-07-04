import random
Heads = 0
Tails = 0
print
print "Starting the Coin Toss program.."
for i in range(1,5001):
    toss = round(random.random())
    #print toss
    if toss == 1 :
        winner = "Heads"
        Heads +=1
    else:
        winner = "Tails"
        Tails +=1
    print"Attempt #",i,":   Throwing a coin...it's a ",winner,"! ... Got ",Heads," Heads so far...and ",Tails," Tails so far"

total = Heads + Tails
print total, (Heads / total)
print "Program ending, no more coin tosses..  Result:::    Heads:",(Heads),"%      Tails:",Tails,"%"
print