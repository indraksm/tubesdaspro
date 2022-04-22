def tambah_game():
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok = input("Masukkan stok awal: ")
    
    while (nama == "" or kategori == "" or tahun == "" or harga == "" or stok == ""):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok = input("Masukkan stok awal: ")
    
    if (nama != "" and kategori != "" and tahun != "" and harga != "" and stok != ""):
        print("Selamat! Berhasil menambahkan game", (nama))

    