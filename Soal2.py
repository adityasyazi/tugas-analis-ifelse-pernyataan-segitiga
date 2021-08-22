print("+========Program Menentukan Jenis Segitiga=========+")
print("|Tugas Soal 2                                      |")
print("|Nama  : Yazi Adityas                              |")
print("|Kelas : XB M.Kom                                  |")
print("|NIM   : 2111600447                                |")
print("+==================================================+")
print(" ")
#invalid_input = True
#def start() :
while True:
    sisi1 = input("Masukan Sisi Pertama : ")
    sisi2 = input("Masukan Sisi Kedua : ")
    sisi3 = input("Masukan Sisi Ketiga : ")

    print("Seigitiga tersebut merupakan Segitiga ")

    if sisi1 == sisi2 and sisi1 == sisi3:
        print("Sama Sisi")
    elif sisi1==sisi2 or sisi2==sisi3 or sisi3==sisi1:
        print("Sama Kaki")
    else:
        print("Sembarang")

#while invalid_input:  # this will loop until invalid_input is set to be True
#    start()
    print(" ")

    # your code
    cont = input("Coba Lagi? iya/tidak > ")
    while cont.lower() not in ("iya","tidak"):
        cont = input("Another one? yes/no > ")
    if cont == "tidak":
        break
