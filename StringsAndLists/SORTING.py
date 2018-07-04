def mysort(arr):
    max= 0
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                max = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = max
    print arr                
    return arr

x = [5,4,3,2,1,78,54,2,1,2]
mysort(x)
