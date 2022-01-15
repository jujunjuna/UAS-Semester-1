from model.daftar_nilai import *
from view.view_nilai import *

print("===============================================================")
print("|                PROGRAM INPUT NILAI MAHASISWA                |")
print("===============================================================")

while True:
    print("\n")
    menu = input("1 = tambah \n2 = lihat \n3 = Hapus \n4 = cari \n5 = ubah \n6 = keluar\nPilih Menu: ")
    print ("\n")

    if menu == "1" :
        tambah_data()
    elif menu == "2" :
        lihat_data()
    elif menu == "3" :
        hapus_data()
    elif menu == "4" :
        cari_data()
    elif menu == "5" :
        ubah_data()
    elif menu == "6" :
        break
    else:
        print("Input yang anda masukan salah coba ulangi")
