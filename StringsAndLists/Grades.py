
# 10 scores between 60 & 100
def grade(score):
    if( 60 <= score <= 69):
        grade = "D"
    elif(70 <= score <=79):
        grade = "C"
    elif(80 <= score <=89):
        grade = "B"
    elif(90 <= score <=100):
        grade = "A"
    else:
        grade = "F"    
    return grade    

import random
print "Grades & Scores"
for i in range(0,10):
    score = int((random.random() *40) + 61)  # 60 or 61 ???
    print "Score: ",score,";  Your Grade is ", grade(score)
print "End of the Program. Bye!"



#print grade(65)    