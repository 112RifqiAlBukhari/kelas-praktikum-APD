# nama = ["shandy,"106,True,
#         ["yuyun",145]3.96,
#         [123,"ALVITO",False,3.66],
#         "rehan"]
# print(nama[5][0])
# matkul = ["APD",
#           "APL",
#           "WEB",
#           "JARKOM",
#           "BASDAT",
#           "STURKDAT",
#           "PTI",
#           "KALKULUS",
#           "PROBAS"
# ]
# print(matkul[6])
# print(nama[2])
# makanan = ["bakso","sate","soto","nasi goreng","mie goreng","mie ayam","aym bakar","cumi goreng"]
# print("sebelum : ")
# # print(makanan)
# # print(makanan[:2])
# # makanan.append("nasi goreng")
# print("sesudah: ")
# makanan.clear()
# print(makanan)

#del makanan[2]
# data = makanan.pop(5)
# print(makanan)
# # print(makanan)
# # makanan.insert(2,"nasi goreng")
# # makanan[2] = ["ayam","bebek"]
# print(makanan)
# print(data)

# minuman = ["hilo","milo","susu","josu","kawa kawa","sirup"]
# print("sebelum : ")
# print(minuman)
# del minuman[3]
# #minuman.append = ["jus tomat"]
# print("sesudah : ")
# # 
# minuman[4] = "air putih"
# # print(minuman)
# minuman.insert(0,"jus tomat")
# del minuman[1]
# print(minuman)

# makanan = ["balon","ayam",["bakso","soto","sate","ikan","bebek"]]

# for i in makanan :
#     if isinstance(i,list):
#         for j in i :
#             print(j, end=" ")
#     else:
#         print(i)
# for i in makanan :
#     for j in i :
#         print(j)



akuns=[]

while True:
    print("selamat datang di aplikasi kami")
    print("silahkan pilih 'daftar akun' jika belum buat akun,dan jika sudah memiliki akun silahkan 'login'")
    print("1. daftar akun")
    print("2. login")
    print("3. exit")
    print("_____________________")
    opsi = input("pilih opsi : ")
    print(" ")

    if opsi == "1" :
        print("halo pengguna baru! ayo nuat akun dulu")
        username = input("username :")
        akuna = False
        for akun in  akuns:
            if akuns [0] == username : # memeriksa apakah username sudah ada 
                akunaa= True
                break
        if akuna:
            print("nama sudah terpakai untuk registrasi silahkan coba lagi")
        else:
            password = input("password : ")
            akuna.append([username, password, []]) #simpan username, password, dan catatan(sebagai list kosong)
            print(f"akun anda  berhasil terdaftar dengan ID: {username}")