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

def csv_to_array(dir):
    f = open(dir, 'r')
    raw_data = f.readlines()
    f.close()

    matrix_data = [['']]
    index_matrix = 0

    for line in raw_data:
        index_array = 0

        for c in line:
            if c == ';':
                matrix_data[index_matrix] += ['']
                index_array += 1
            elif c != '\n':
                matrix_data[index_matrix][index_array] += c

        if line != raw_data[-1]: matrix_data += [['']]
        index_matrix += 1

    return matrix_data

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