
def findChars(arr,chr):
    new_list = []
    for i in arr:
        if(isinstance(i,str)):    
            # if(i.find(chr) != -1):
            for j in range(0,len(i)):
                # print i[j]
                if(i[j] == chr):
                    new_list.append(i)
                    break     
    print new_list


findChars([1,2,3,"Hope","Me","ono","two"],"o")           