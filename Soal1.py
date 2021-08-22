print("+==========Program Menghitung nilai Tengah===========+")
print("|Tugas Soal 1                                        |")
print("|Nama  : Yazi Adityas                                |")
print("|Kelas : XB M.Kom                                    |")
print("|NIM   : 2111600447                                  |")
print("+====================================================+")
print(" ")
while True:

    angka1 = input("Masukan Angka Pertama : ")
    angka2 = input("Masukan Angka Kedua : ")
    angka3 = input("Masukan Angka Ketiga : ")

    print("Angka tengah ketiga Angka diatas adalah : ")

    if angka2 < angka1 and angka1 < angka3:
        print(angka1)
    elif angka3 < angka1 and angka1 < angka2:
        print(angka1)

    elif angka3 < angka2 and angka2 < angka1 :
        print(angka2)
    elif angka1 < angka2 and angka2 < angka3:
        print(angka2)

    elif angka2 < angka3 and angka3 < angka1:
        print(angka3)
    elif angka1 < angka3 and angka3 < angka2:
        print(angka3)

    else:
        print ("Angka yang dimasukan salah (Error)")
    print(" ")

    cont = input("Coba Lagi? iya/tidak > ")
    while cont.lower() not in ("iya","tidak"):
        cont = input("Beneran mau coba? iya/tidak > ")
    if cont == "tidak":
        break
