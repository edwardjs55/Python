words = "It's Thanksgiving day. It's my birthday, too!"
daypos = words.find("day")
print daypos
newwords = words.replace("day","month")
print newwords

x = [2,54,-2,7,12,98]
max = max(x)
min = min(x)
print x,"     Max : ",max,"    Min : ",min
x = [19,2,54,-2,7,12,98,32,10,-3,6]
first = x[0]
last = x[len(x)-1]
print x,"   First: ",first,"   Last: ",last

x = sorted(x)
print x

# swap Halves
length = len(x)/2
fh = x[:length]
lh = x[length:]
z = lh + fh
print z, "  Swapped halfzies...."

