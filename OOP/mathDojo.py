class mathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self,*args):
        #get Args list
        #Addem UP
        print args
        # if len(args) == 0:
        #      return self
        # if len(args) == 1:
        #      self.result += args[0]
        # if len(args) >= 2:
        #     for i in range(0,len(args)):
        #         self.result += args[i] 
        for i in range(0,len(args)):
            #print "i = ",i
            if type(args[i]) == int :
                self.result += args[i]
            elif type(args[i]) in [list,tuple] :
                for j in range(0,len(args[i])):
                    self.result += args[i][j]
            
            # elif type(args[i]) == tuple :
            #     for j in range(0,len(args[i])):
            #         self.result += args[i][j]
        print self.result
        return self

    def subtract(self,*args):
        #get Args list
        # Subtract
        # update self.result

        # print args
        # if len(args) == 0:
        #      return self
        # if len(args) == 1 and type(args) == int :
        #      self.result -= args[0]
        # if len(args) >= 2:
        #     for i in range(0,len(args)):
        #         self.result -= args[i] 

        for i in range(0,len(args)):
            #print "i = ",i
            if type(args[i]) == int :
                self.result -= args[i]
            elif type(args[i]) in [list,tuple] :
                for j in range(0,len(args[i])):
                    self.result -= args[i][j]  
        print self.result
        return self

math = mathDojo()
# math.add(3,4,5)
# math.subtract(5)
# math.add(8).result
# math.result

# md = mathDojo()
# value = (md.add(2).add(2,5).subtract(3,2).result)
# print "Assignment Results : ", value

math.subtract().add(1,2,[3,4,5],1,2,[7,8],(5,5)).add().subtract(6,3,(5,5),[1,2]).result
