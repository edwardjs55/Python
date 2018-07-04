
# Multipes section
# Odd numbers
i =1
for i in range(1,1000,2):
    print i

i= 5
#for i in range(5,1000000,5):
    # print i    # it works..but toom uch time...
sum = 0
a = [1,2,5,10,255,3]
for i in a:
    sum = sum + i
    # print i
print "Sum = ",sum  

average = sum/len(a)  
print "average: ",average,'     sum: ',sum,'    length: ',len(a)
