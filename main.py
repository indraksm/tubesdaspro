import pandas as pd
df1 = pd.read_csv('user.csv')
df2 = pd.read_csv('game.csv')
df3 = pd.read_csv('kepemilikan.csv')
df4 = pd.read_csv('riwayat.csv')


end = False
while end == False:
    pilih = input(">>>")
    user = []
    passw = []
    admin = []
    log = False
    jadiUser = False
    jadiAdmin = False
    
    #F02 Register
    if pilih == "register":
        nama = input("Masukan nama: ")
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        print('Username', username, 'telah berhasil register ke dalam "Binomo" ')
        jadiUser = True
        user = user + [username]
        passw = passw + [password]
        for i in range(len(user)):
            if username == user[i]:
                print("Username", username, "sudah terpakai, silahkan menggunakan username lain")

    #F02 Login
    elif pilih == "login":
        a = input("Masukkan username: ")
        b = input("Masukkan password: ")
        for i in range(len(user)):
            if a == user[i] and b == passw[i]:
                print("Halo", nama, '! Selamat datang di "Binomo" ')
                log = True
            else:
                print("Password atau username salah atau tidak ditemukan")

    elif pilih == "mencoba_sesuatu":
        if log == False:
            print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain login")

    elif pilih == "hanya_user":
        if jadiUser == False:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    
    elif pilih == "hanya_admin":
        if jadiAdmin == False:
            print("Maaf anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")