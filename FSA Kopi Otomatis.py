from os import system
def menu():
    print("======== Mesin Pembuat Kopi Otomatis ========\n")
    amt = False
    while amt == False:
        system('cls')
        print("Jenis Minuman : ")
        print("1. Coffee")
        print("2. Milk")
        print("3. Chocolate")
        print("4. Coffee Milk")
        print("5. Choco Coffee")
        print("6. Mocca")
        print("7. Choco Milk")
        print("8. Restart")
        amtCat = int(input("Masukan Jenis Minuman (1 - 8) : "))
        if amtCat == 1:
            jenis = "Coffee"
            amt = True
        elif amtCat == 2:
            jenis = "Milk"
            amt = True
        elif amtCat == 3:
            jenis = "Chocolate"
            amt = True
        elif amtCat == 4:
            jenis = "Coffee Milk"
            amt = True
        elif amtCat == 5:
            jenis = "Choco Coffee"
            amt = True
        elif amtCat == 6:
            jenis = "Mocca"
            amt = True
        elif amtCat == 7:
            jenis = "Choco Milk"
            amt = True
        elif amtCat == 8:
            menu()
        else :
            print("Pilihan yang anda masukkan salah.")
            print("Coba lagi!")
            amt = False
    pil = False
    while pil == False:
        system('cls')
        print("Pilih Jenis Ukuran Cup :")
        print("1. Kecil   (S)")
        print("2. Sedang  (M)")
        print("3. Besar   (L)")
        gelas = int(input("(1-3): "))
        if gelas == 1:
            gname = "Kecil"
            pil = True
        elif gelas == 2:
            gname = "Sedang"
            pil = True
        elif gelas == 3:
            gname = "Besar"
            pil = True
        else :
            print("Nilai yang anda masukkan salah!")
            print("Silahkan pilih kembali (1-3): ")
            pil = False
    add = False
    while add == False :
        system('cls')
        print("Tambahan Pada Minuman : ")
        print("1. Gula")
        print("2. Kopi")
        print("3. Susu")
        print("4. Coklat")
        print("5. Tidak Ada")
        print("6. Restart")
        addCat = int(input("Input Tambahan (1-6): "))
        if addCat == 1:
            more = "Gula"
            add = True
        elif addCat == 2:
            more = "Kopi"
            add = True
        elif addCat == 3:
            more = "Susu"
            add = True
        elif addCat == 4:
            more = "Coklat"
            add = True
        elif addCat == 5:
            more = "-"
            add = True
        elif addCat == 6:
            menu()
        else :
            print("Pilihan yang anda masukkan salah.")
            print("Coba lagi!")
            add = False
    finalState = False
    while finalState == False:
        system('cls')
        print("Rincian Minuman: ")
        print("Jenis Minuman : " + jenis)
        print("Ukuran gelas  : " + gname )
        print("Tambahan      : " + more)
        print("\nApakah Sudah Sesuai?")
        print("1. Sesuai")
        print("2. Ulangi dari Awal")
        end = int(input("Input : "))
        if end == 1:
            finalState = True
            system('cls')
            print( jenis + " ukuran " + gname + " dengan tambahan " + more)
            print("\nMinuman Sedang diproses, Mohon Bersabar\n== Arigato Gozaimasu ==")
            exit()
        elif end == 2:
            menu()
        else :
            print ("Salah Input")
            finalState = False
menu()
