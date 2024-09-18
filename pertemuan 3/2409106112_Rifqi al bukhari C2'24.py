cuaca = "mendung"
if cuaca == "cerah":
    print("Kamu pergi keluar rumah")

else:
    print("hari ini mendung")

Umur = int(input("Masukkan umur Anda : "))
if Umur >0:              
    if Umur <= 10:
        print( "Umur Anda termasuk kategori anak-anak")
    elif Umur <= 18:
        print( "Umur Anda termasuk kategori remaja")
    elif Umur <=35:
        print("Umur Anda termasuk kategori dewasa")
    elif Umur <=65:
        print("Umur Anda termasuk kategori paruh baya")
    else:
        print("Umur Anda termasuk kategori Tua")
else:
    print("umur harus bilangan positif") 

nim = int(input("masukkan nim : "))
if nim >= 1 and nim <=50 :
    if nim >=1 and nim <=25 :
        print("kelas A'1")
    else:
        print("kelas a'2")
elif nim >= 51 and nim <= 100 :
    if nim >=51 and nim <= 75 :
        print("kelas b'1")
    else:
        print("kelas b'2")   
elif nim >=101 and nim <= 121 :
    if nim >=101 and nim <= 110 :
        print("kelas c'2")        
    else:
        print("kelas c'2")    
else:
    print("anda anomali")   

angka = int(input("Masukkan angka: "))
hasil = "kelas a" if nim >=1 and nim<=50 else "kelas b" if nim >=51 and nim <=100 else "kelas c" if nim >= 101 and nim <=121 else "mahasiswa ghaib"
print(hasil)