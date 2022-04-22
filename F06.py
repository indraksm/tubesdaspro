def ubah_stok():
    id = input("Masukkan id game: ")
    if id  not in (game.csv):
        print("Tidak ada game dengan ID tersebut!")
    else:
        jumlah = input("Masukkan jumlah: ")
        skrg = int(stok) + int(jumlah)
        if jumlah < 0:
            if stok < abs(jumlah):
                print("Stok game", nama, "gagal dikurangi karena stok kurang. Stok sekarang:", stok)
            else:
                print("Stok game", nama,"berhasil dikurangi. Stok sekarang:", skrg)
        elif jumlah > 0:
            print("Stok game", nama,"berhasil ditambahkan. Stok sekarang:", skrg)
