def input_nama():
    print("Masukan Data Mahasiswa")
    global nama
    nama = input("Nama: ")
    return nama

def input_nim():
    global nim
    nim = input("Nim: ")
    return nim

def input_tugas():
    global nilai_tugas
    nilai_tugas = int(input("Masukan nilai tugas: "))
    return nilai_tugas

def input_uts():
    global nilai_uts
    nilai_uts = int(input("Masukan nilai uts: "))
    return nilai_uts

def input_uas():
    global nilai_uas
    nilai_uas = int(input("Masukan nilai uas: "))
    return nilai_uas

def akhir():
    global nilai_akhir
    nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100
    return nilai_akhir

