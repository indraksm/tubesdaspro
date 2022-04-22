import time
from tkinter import N

def panjang(listx):
    n = 0
    for i in listx:
        n += 1
    return n

def kerangajaib():

    jawaban = ["Iya", "Tidak", "Yooo ndak tahu kok tanya saya", "sabeb", "masa sihh", "mau", "ah gatau males pengen beli truk", "yakali", "o aja", 
            "gantengg", "tanya aja ke tembok", "naon yakkk"]
    length = panjang(jawaban)

    input("Apa pertanyaanmu? ")

    local = time.localtime()
    now = time.strftime("%S", local)

    a = 10
    b = 29
    m = 31
    
    count = 0
    loop = True
    now = int(now)                  
    while (count < 7 or loop == True):                          
        if (count >= 7 and (0 <= result <= (length-1))):        
            loop = False
        else:                                   
            result = ((now*a)+b)%m
            now = result                    
            count +=1
        
    print(jawaban[result])

kerangajaib()