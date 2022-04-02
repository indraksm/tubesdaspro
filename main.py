from tkinter import FALSE
import pandas as pd

df1 = pd.read_csv('user.csv', sep = ";")
df2 = pd.read_csv('game.csv', sep = ";")
df3 = pd.read_csv('kepemilikan.csv', sep = ";")
df4 = pd.read_csv('riwayat.csv', sep = ";")

#Untuk syarat Register Username dan Password
huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "0123456789_-"
    
#F02 Register
def register():
    sama = False
    valid = True
    jadiUser = False
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    for i in df1["username"]:
        if i == username:
            sama = True

    if sama == True:
        print("Username", username, "sudah terpakai, silahkan gunakan username lain")

    else:
        for i in username:
            if (i not in huruf) and (i not in huruf.lower()) and (i not in angka):
                valid = False
        if valid == False:
            print("Username", username, "tidak valid")
        else:
            print("Username", username, 'telah berhasil register ke dalam "Binomo".')
            jadiUser = True
            if jadiUser == True:
                role = "User"
            
        
            datauser = {"username" : [username],
                        "nama" : [nama],
                        "password" : [password],
                        "role" : [role],
                        "saldo" : []
            }
    df1 = pd.DataFrame(data=datauser)

        
        
    
#F03 Login
def login():
    

elif pilih == "mencoba_sesuatu":
    if log == False:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain login")

elif pilih == "hanya_user":
    if jadiUser == False:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    
elif pilih == "hanya_admin":
    if jadiAdmin == False:
        print("Maaf anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")