def Login():
    loguser = str(input("Masukan user: "))
    logpass = str(input("Masukkan pass: "))
    f = list(open('user.csv', 'r'))
    k = 0 # Indeks user pada csv file
    j = 0 # Indeks password pada csv file
    a = -1 # Validasi user sesuai dengan password
    b = -2 # Validasi password sesuai dengan user
    validuser = False
    validpass = False
    successful = False
    loggeduser = ''
    for i in f:
        if (splitFunc(i)[1] != loguser):
            #print('Ini k: ',k)
            k += 1
            #print(f'({splitFunc(i)[1]}) = ({loguser})')
        if (splitFunc(i)[1] == loguser):
            #print('k berhasil: ',k)
            #print(' isi k:',splitFunc(i)[1])
            validuser = True
            a = k
    for x in f:
        if ((splitFunc(x)[3]) != logpass) and ((splitFunc(x)[3]) != logpass+"\n"):
            #print('Ini j: ',j)
            j += 1
            #print(f'({(splitFunc(x)[2])}) = ({logpass})')
        if ((splitFunc(x)[3]) == logpass+"\n") or ((splitFunc(x)[3] == logpass)):
            #print('j berhasil: ',j)
            #print(' isi j:',splitFunc(x)[2])
            validpass = True
            b = j
    if (a == b):
        successful = True
    if (validuser == True) and (validpass == True) and (successful == True):
        print(f'Halo {(splitFunc(f[a])[2])}! Selamat datang di “Binomo”.')
        loggeduser = loguser
        return loggeduser, successful # Memberikan nama username, serta validasi logged in (successful optional)
    else: #(successful == False):
        print('Password atau username salah atau tidak ditemukan.')
        return successful == False # Belum logged-in.

def splitFunc(x): # Split 6 kata
    first_val = ''
    second_val = ''
    third_val = ''
    fourth_val = ''
    fifth_val = ''
    sixth_val = ''
    i = 0
    terminate_search = False

    while (terminate_search != True): #Mendapatkan first_val (ID)
        if (x[i] != ','):
            first_val += x[i]
            i += 1
        else:
            while (terminate_search != True): # Mendapatkan second_val (username)
                if (x[i+1] != ','):
                    second_val += x[i+1]
                    i += 1
                else:
                    while(terminate_search != True): # Mendapatkan third_val (nama)
                        if(x[i+2] != ','):
                            third_val += x[i+2]
                            i +=1
                        else:
                            while(terminate_search != True): # Mendapatkan fourth_val (password)
                                if(x[i+3] != ','):
                                    fourth_val += x[i+3]
                                    i+=1
                                else:
                                    while(terminate_search != True): # Mendapatkan fifth_val (role)
                                        if(x[i+4] != ','):
                                            fifth_val += x[i+4]
                                            i+=1
                                        else:
                                            while(terminate_search != True): # Mendapatkan sixth_val (saldo)
                                                if(x[i+5] != ','):
                                                    sixth_val += x[i+4+1:]
                                                    terminate_search = True
    return(first_val, second_val, third_val, fourth_val, fifth_val, sixth_val)