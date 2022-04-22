def length(listx):
    n = 0
    for i in listx:
        n += 1
    return n

def sortlist(x):
    for i in range(length(x) -1):
        for j in range(length(x) -i -1):
            if x[j] > x[j+1] :          
                sementara = x[j]                         
                x[j] = x[j+1]
                x[j+1] = sementara

