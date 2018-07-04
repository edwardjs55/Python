class Call(object):
    def __init__(self,name,time,phone,reason,id):
        self.id = id
        self.name = name
        self.call_time = time
        self.phone = phone
        self.reason = reason

    def displayCall(self):
        print "Caller: ", self.name,'   time:',self.call_time,'   Phone:',self.phone,'   reason:',self.reason,'   call ID: ',self.id
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0 # of calls in queye

    def addCall(self,call): # add a call to the end of the que list
        self.calls.append(call)
        self.queue = len(self.calls)

    def addCalls(self,*calls):  # add mutiple calls in one command
        for call in calls:
            self.calls.append(call)
        self.queue = len(self.calls)    

    def RemoveCall(self,call):
        # find call id in self.queue and remove it
        self.calls.remove(call)
        self.queue = len(self.calls)
        

    def info(self):
        # print name and phone for each Call in the queue AND queue length
        # loop through self.queue amd print info
        print 'Current Calls in the Queue: ', self.queue
        for call in self.calls:
            # call.displayCall()
            print 'Name: ', '%-20s' % call.name,' Phone: ', call.phone
        
##         DO IT!!!!
# 

call1 = Call('Mrs Jones','12:00','214-666-7878','Cat in tree',1)
call2 = Call('Mr Jones', '1:00','214-666-7878', 'wife calling abouy Cat in tree',2)
call3 = Call('Ralphie Jones','1:15','214-666-7878','locked parents out of house, going back to bed',3)
call4 = Call('Emma Jones','1:20','214-666-7878','I want my Mommy and my Teddy Bear', 4)

call1.displayCall()
call2.displayCall()
call3.displayCall()

Help = CallCenter()
#Help.addCall(call1)
#Help.addCall(call2)
#Help.addCall(call3)
Help.addCalls(call1,call2,call3,call4)
# print Help.calls

# print Help.queue
print
Help.info()
print 'Remove call1'
Help.RemoveCall(call1)
Help.info()





    